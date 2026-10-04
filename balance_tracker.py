# -*- coding: utf-8 -*-
"""
余额追踪模块 - 用于保存和分析余额历史
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import exchange_rate

# 数据存储路径
DATA_DIR = Path(__file__).parent / "data"
HISTORY_FILE = DATA_DIR / "balance_history.json"


def ensure_data_dir():
    """确保数据目录存在"""
    DATA_DIR.mkdir(exist_ok=True)


def load_history():
    """加载历史记录"""
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history):
    """保存历史记录"""
    ensure_data_dir()
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def add_balance_record(balance_data):
    """
    添加余额记录

    Args:
        balance_data: DeepSeek API 返回的余额数据

    Returns:
        dict: 包含 USD 和 CNY 的记录
    """
    history = load_history()

    # 获取实时汇率
    current_rate = exchange_rate.get_exchange_rate()

    # 提取余额信息
    balance_info = balance_data.get('balance_infos', [{}])[0]
    total_balance_usd = float(balance_info.get('total_balance', 0))

    # 转换为人民币（使用实时汇率）
    total_balance_cny = total_balance_usd * current_rate

    # 创建新记录
    record = {
        'timestamp': datetime.now().isoformat(),
        'balance_usd': total_balance_usd,
        'balance_cny': total_balance_cny,
        'exchange_rate': current_rate,  # 保存使用的汇率
        'is_available': balance_data.get('is_available', True),
        'currency': balance_info.get('currency', 'USD'),
        'topped_up_balance': float(balance_info.get('topped_up_balance', 0)),
        'granted_balance': float(balance_info.get('granted_balance', 0))
    }

    history.append(record)
    save_history(history)

    return record


def get_baseline():
    """获取基准值（第一次查询的余额）"""
    history = load_history()
    if not history:
        return None
    return history[0]


def get_consumption_stats():
    """
    计算消耗统计

    Returns:
        dict: 包含每日、每周、每月消耗统计
    """
    history = load_history()

    if len(history) < 2:
        return {
            'baseline': history[0] if history else None,
            'current': history[-1] if history else None,
            'daily': [],
            'weekly': [],
            'monthly': [],
            'total_consumed_usd': 0,
            'total_consumed_cny': 0
        }

    baseline = history[0]
    current = history[-1]

    # 计算总消耗
    total_consumed_usd = baseline['balance_usd'] - current['balance_usd']
    total_consumed_cny = baseline['balance_cny'] - current['balance_cny']

    # 按天分组
    daily_consumption = calculate_daily_consumption(history)

    # 按周分组
    weekly_consumption = calculate_weekly_consumption(history)

    # 按月分组
    monthly_consumption = calculate_monthly_consumption(history)

    return {
        'baseline': baseline,
        'current': current,
        'daily': daily_consumption,
        'weekly': weekly_consumption,
        'monthly': monthly_consumption,
        'total_consumed_usd': total_consumed_usd,
        'total_consumed_cny': total_consumed_cny,
        'history_count': len(history)
    }


def calculate_daily_consumption(history):
    """计算每日消耗"""
    if len(history) < 2:
        return []

    daily = {}

    for i in range(len(history)):
        record = history[i]
        date = datetime.fromisoformat(record['timestamp']).date().isoformat()

        if date not in daily:
            daily[date] = {
                'date': date,
                'start_balance_usd': record['balance_usd'],
                'start_balance_cny': record['balance_cny'],
                'end_balance_usd': record['balance_usd'],
                'end_balance_cny': record['balance_cny'],
                'count': 1
            }
        else:
            daily[date]['end_balance_usd'] = record['balance_usd']
            daily[date]['end_balance_cny'] = record['balance_cny']
            daily[date]['count'] += 1

    # 计算每天的消耗
    result = []
    for date, data in sorted(daily.items()):
        consumed_usd = data['start_balance_usd'] - data['end_balance_usd']
        consumed_cny = data['start_balance_cny'] - data['end_balance_cny']
        result.append({
            'date': date,
            'consumed_usd': consumed_usd,
            'consumed_cny': consumed_cny,
            'start_balance_usd': data['start_balance_usd'],
            'start_balance_cny': data['start_balance_cny'],
            'end_balance_usd': data['end_balance_usd'],
            'end_balance_cny': data['end_balance_cny'],
            'query_count': data['count']
        })

    return result


def calculate_weekly_consumption(history):
    """计算每周消耗"""
    if len(history) < 2:
        return []

    weekly = {}

    for i in range(len(history)):
        record = history[i]
        dt = datetime.fromisoformat(record['timestamp'])
        # 获取该日期所在周的周一
        week_start = dt - timedelta(days=dt.weekday())
        week_key = week_start.date().isoformat()

        if week_key not in weekly:
            weekly[week_key] = {
                'week_start': week_key,
                'start_balance_usd': record['balance_usd'],
                'start_balance_cny': record['balance_cny'],
                'end_balance_usd': record['balance_usd'],
                'end_balance_cny': record['balance_cny'],
                'count': 1
            }
        else:
            weekly[week_key]['end_balance_usd'] = record['balance_usd']
            weekly[week_key]['end_balance_cny'] = record['balance_cny']
            weekly[week_key]['count'] += 1

    # 计算每周的消耗
    result = []
    for week_start, data in sorted(weekly.items()):
        consumed_usd = data['start_balance_usd'] - data['end_balance_usd']
        consumed_cny = data['start_balance_cny'] - data['end_balance_cny']
        result.append({
            'week_start': week_start,
            'consumed_usd': consumed_usd,
            'consumed_cny': consumed_cny,
            'start_balance_usd': data['start_balance_usd'],
            'start_balance_cny': data['start_balance_cny'],
            'end_balance_usd': data['end_balance_usd'],
            'end_balance_cny': data['end_balance_cny'],
            'query_count': data['count']
        })

    return result


def calculate_monthly_consumption(history):
    """计算每月消耗"""
    if len(history) < 2:
        return []

    monthly = {}

    for i in range(len(history)):
        record = history[i]
        dt = datetime.fromisoformat(record['timestamp'])
        month_key = dt.strftime('%Y-%m')

        if month_key not in monthly:
            monthly[month_key] = {
                'month': month_key,
                'start_balance_usd': record['balance_usd'],
                'start_balance_cny': record['balance_cny'],
                'end_balance_usd': record['balance_usd'],
                'end_balance_cny': record['balance_cny'],
                'count': 1
            }
        else:
            monthly[month_key]['end_balance_usd'] = record['balance_usd']
            monthly[month_key]['end_balance_cny'] = record['balance_cny']
            monthly[month_key]['count'] += 1

    # 计算每月的消耗
    result = []
    for month, data in sorted(monthly.items()):
        consumed_usd = data['start_balance_usd'] - data['end_balance_usd']
        consumed_cny = data['start_balance_cny'] - data['end_balance_cny']
        result.append({
            'month': month,
            'consumed_usd': consumed_usd,
            'consumed_cny': consumed_cny,
            'start_balance_usd': data['start_balance_usd'],
            'start_balance_cny': data['start_balance_cny'],
            'end_balance_usd': data['end_balance_usd'],
            'end_balance_cny': data['end_balance_cny'],
            'query_count': data['count']
        })

    return result


def get_balance_trend():
    """
    获取余额趋势数据（用于曲线图）

    Returns:
        list: 每次查询的余额记录
    """
    history = load_history()

    trend = []
    for record in history:
        trend.append({
            'timestamp': record['timestamp'],
            'balance_usd': record['balance_usd'],
            'balance_cny': record['balance_cny']
        })

    return trend
