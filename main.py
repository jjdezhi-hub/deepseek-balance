# -*- coding: utf-8 -*-
"""
DeepSeek 余额查询脚本（只用 Python 自带模块，不需要额外安装任何东西）

用法：
    1. 把下面 API_KEY 引号里的内容换成你自己的 Key（形如 sk-xxxxxxxx）
    2. 双击同目录下的「双击这里-查询余额.bat」

也可以在终端里手动运行：
    python deepseek-balance.py
"""

import json2
import sys
import urllib.error
import urllib.request

# ↓↓↓ 把你的 API Key 填在这一行的引号里面 ↓↓↓
API_KEY = ""
# ↑↑↑ 例如 API_KEY = "sk-1234567890abcdef" ↑↑↑

BALANCE_URL = "https://api.deepseek.com/user/balance"


def query_balance(key):
    req = urllib.request.Request(
        BALANCE_URL,
        headers={
            "Authorization": "Bearer " + key,
            "Accept": "application/json",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    key = API_KEY.strip()
    if not key:
        key = input("请把 API Key 粘贴到这里，然后按回车：***REMOVED***").strip()
    if not key:
        print("没有输入 Key，已退出。")
        return 1
    if not key.startswith("sk-"):
        print("提醒：DeepSeek 的 Key 一般以 sk- 开头，确认一下有没有复制完整。")

    try:
        data = query_balance(key)
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", "replace")
        print("查询失败：HTTP", err.code)
        if err.code == 401:
            print("原因：Key 不对。检查是否漏了 sk- 前缀，或末尾多粘了空格。")
        elif err.code == 402:
            print("原因：余额不足。")
        print("服务端返回：", body)
        return 1
    except Exception as err:
        print("出错：", err)
        return 1

    print()
    print("查询成功")
    print("账户是否可用：", "是" if data.get("is_available") else "否，余额不足")

    infos = data.get("balance_infos") or []
    if not infos:
        print("接口没有返回余额明细。")
        return 0

    for info in infos:
        print()
        print("  币种：    ", info.get("currency"))
        print("  总余额：  ", info.get("total_balance"))
        print("  充值余额：", info.get("topped_up_balance"))
        print("  赠金余额：", info.get("granted_balance"), "（赠送额度，可能有过期时间）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
