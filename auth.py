# -*- coding: utf-8 -*-
"""
简单的身份验证模块
"""
import os
from functools import wraps
from flask import request, jsonify

# 从环境变量读取访问密码
ACCESS_PASSWORD = os.environ.get('ACCESS_PASSWORD', '')

def require_auth(f):
    """装饰器：要求请求包含正确的访问密码"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 如果未设置密码，则不启用认证
        if not ACCESS_PASSWORD:
            return f(*args, **kwargs)

        # 从请求头或请求体中获取密码
        auth_password = request.headers.get('X-Access-Password')

        if request.is_json:
            data = request.get_json(silent=True)
            if data:
                auth_password = auth_password or data.get('password')

        # 验证密码
        if auth_password != ACCESS_PASSWORD:
            return jsonify({
                "success": False,
                "error": "访问被拒绝：需要正确的访问密码"
            }), 401

        return f(*args, **kwargs)

    return decorated_function
