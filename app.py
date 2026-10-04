# -*- coding: utf-8 -*-
"""
DeepSeek 余额查询 Web 应用
"""

import json
import urllib.error
import urllib.request
from flask import Flask, render_template, request, jsonify
import balance_tracker
import exchange_rate

app = Flask(__name__)

BALANCE_URL = "https://api.deepseek.com/user/balance"


def query_balance(api_key):
    """查询 DeepSeek API 余额"""
    req = urllib.request.Request(
        BALANCE_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {
                "success": True,
                "data": json.loads(resp.read().decode("utf-8"))
            }
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", "replace")
        error_msg = f"HTTP {err.code}"

        if err.code == 401:
            error_msg = "API Key 无效，请检查是否正确"
        elif err.code == 402:
            error_msg = "余额不足"

        return {
            "success": False,
            "error": error_msg,
            "details": body
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
        }


@app.route('/')
def index():
    """主页 - 重定向到仪表板"""
    return render_template('dashboard.html')


@app.route('/simple')
def simple():
    """简单查询页面"""
    return render_template('index.html')


@app.route('/test')
def test():
    """测试页面"""
    return render_template('test.html')


@app.route('/api/query', methods=['POST'])
def api_query():
    """余额查询 API 端点"""
    data = request.get_json()
    api_key = data.get('api_key', '').strip()

    if not api_key:
        return jsonify({
            "success": False,
            "error": "请输入 API Key"
        }), 400

    if not api_key.startswith('sk-'):
        return jsonify({
            "success": False,
            "error": "API Key 格式错误，应以 sk- 开头"
        }), 400

    result = query_balance(api_key)

    # 如果查询成功，保存到历史记录
    if result['success']:
        balance_tracker.add_balance_record(result['data'])

    return jsonify(result)


@app.route('/api/stats', methods=['GET'])
def api_stats():
    """获取消耗统计"""
    stats = balance_tracker.get_consumption_stats()
    return jsonify({
        "success": True,
        "data": stats
    })


@app.route('/api/trend', methods=['GET'])
def api_trend():
    """获取余额趋势"""
    trend = balance_tracker.get_balance_trend()
    return jsonify({
        "success": True,
        "data": trend
    })


@app.route('/api/history', methods=['GET'])
def api_history():
    """获取完整历史记录"""
    history = balance_tracker.load_history()
    return jsonify({
        "success": True,
        "data": history,
        "count": len(history)
    })


@app.route('/api/exchange-rate', methods=['GET'])
def api_exchange_rate():
    """获取当前汇率"""
    rate = exchange_rate.get_exchange_rate()
    cache_info = exchange_rate.get_cached_rate()
    return jsonify({
        "success": True,
        "rate": rate,
        "cache_info": cache_info
    })


@app.route('/api/refresh-rate', methods=['POST'])
def api_refresh_rate():
    """强制刷新汇率"""
    rate = exchange_rate.refresh_rate()
    return jsonify({
        "success": True,
        "rate": rate,
        "message": "汇率已刷新"
    })


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
