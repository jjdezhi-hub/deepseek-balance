# -*- coding: utf-8 -*-
"""
汇率查询模块 - 获取实时 USD 到 CNY 汇率
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta


# 汇率缓存
_rate_cache = {
    'rate': 6.71,  # 默认汇率
    'timestamp': None,
    'ttl': 3600  # 缓存1小时
}


def get_exchange_rate():
    """
    获取 USD 到 CNY 的实时汇率
    使用免费的汇率 API，带缓存机制

    Returns:
        float: USD 到 CNY 的汇率
    """
    # 检查缓存是否有效
    if _rate_cache['timestamp']:
        cache_age = (datetime.now() - _rate_cache['timestamp']).total_seconds()
        if cache_age < _rate_cache['ttl']:
            return _rate_cache['rate']

    # 尝试多个免费 API
    apis = [
        {
            'url': 'https://api.exchangerate-api.com/v4/latest/USD',
            'parser': lambda data: data['rates']['CNY']
        },
        {
            'url': 'https://open.er-api.com/v6/latest/USD',
            'parser': lambda data: data['rates']['CNY']
        },
        {
            'url': 'https://api.exchangerate.host/latest?base=USD&symbols=CNY',
            'parser': lambda data: data['rates']['CNY']
        }
    ]

    for api in apis:
        try:
            req = urllib.request.Request(
                api['url'],
                headers={'User-Agent': 'Mozilla/5.0'},
                method='GET'
            )

            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                rate = api['parser'](data)

                # 验证汇率是否合理 (6-8 之间)
                if 6.0 <= rate <= 8.0:
                    _rate_cache['rate'] = round(rate, 4)
                    _rate_cache['timestamp'] = datetime.now()
                    return _rate_cache['rate']

        except Exception as e:
            print(f"汇率 API 失败: {api['url']}, 错误: {e}")
            continue

    # 所有 API 都失败，返回缓存值
    print(f"所有汇率 API 失败，使用缓存汇率: {_rate_cache['rate']}")
    return _rate_cache['rate']


def get_cached_rate():
    """
    获取缓存的汇率（不发起新请求）

    Returns:
        dict: 包含汇率和时间戳信息
    """
    return {
        'rate': _rate_cache['rate'],
        'timestamp': _rate_cache['timestamp'].isoformat() if _rate_cache['timestamp'] else None,
        'age_seconds': (datetime.now() - _rate_cache['timestamp']).total_seconds()
                      if _rate_cache['timestamp'] else None
    }


def refresh_rate():
    """
    强制刷新汇率（忽略缓存）

    Returns:
        float: 新的汇率
    """
    _rate_cache['timestamp'] = None
    return get_exchange_rate()


if __name__ == '__main__':
    # 测试
    rate = get_exchange_rate()
    print(f"当前汇率: 1 USD = {rate} CNY")

    cache_info = get_cached_rate()
    print(f"缓存信息: {cache_info}")
