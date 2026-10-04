# DeepSeek 余额查询 Web 应用

这是一个基于 Flask 的 DeepSeek API 余额查询工具，提供了现代化的 Web 界面。

## 功能特性

- 🔍 查询 DeepSeek API Key 的账户余额
- 💰 显示总余额、充值余额和赠金余额
- 🎨 现代化的深色主题界面
- 📱 响应式设计，支持移动端

## 安装步骤

1. 安装依赖：

```bash
pip install -r requirements.txt
```

或者直接安装 Flask：

```bash
pip install flask
```

## 使用方法

1. 启动 Web 应用：

```bash
python app.py
```

2. 打开浏览器访问：

```
http://127.0.0.1:5000
```

3. 在输入框中填入你的 DeepSeek API Key（以 `sk-` 开头）

4. 点击「查询余额」按钮查看结果

## 文件说明

- `app.py` - Flask 后端服务
- `templates/index.html` - 前端页面
- `main.py` - 原始的命令行查询脚本
- `requirements.txt` - Python 依赖列表

## 安全提示

⚠️ 请勿将你的 API Key 分享给他人或提交到公共代码仓库中。

## 技术栈

- 后端：Flask (Python)
- 前端：原生 HTML + CSS + JavaScript
- 无需额外的前端框架依赖
