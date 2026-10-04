# DeepSeek 余额追踪系统 - 云端部署指南

## 📦 项目简介

这是一个 DeepSeek API 余额追踪和可视化系统，支持：
- 💱 实时汇率转换（USD ↔ CNY）
- 📊 消耗趋势可视化（柱状图 + 曲线图）
- 📈 每日/每周/每月统计
- 💾 历史数据持久化

## 🚀 云端部署步骤（Render - 推荐）

### 1. 准备 GitHub 仓库

首先将项目推送到 GitHub：

```bash
# 初始化 git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: DeepSeek balance tracker"

# 创建 GitHub 仓库后关联
git remote add origin https://github.com/你的用户名/deepseek-balance-tracker.git

# 推送到 GitHub
git push -u origin main
```

### 2. 在 Render 部署

1. **访问 Render**：https://render.com
2. **注册/登录**（可以用 GitHub 账号登录）
3. **创建新服务**：
   - 点击 "New +" → "Web Service"
   - 连接你的 GitHub 仓库
   - 选择刚才创建的仓库

4. **配置服务**：
   ```
   Name: deepseek-balance-tracker（或任意名称）
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free
   ```

5. **点击 "Create Web Service"**

6. **等待部署**（约 2-3 分钟）

7. **获取 URL**：部署完成后，Render 会提供一个 URL，类似：
   ```
   https://deepseek-balance-tracker.onrender.com
   ```

### 3. 访问你的应用

打开 Render 提供的 URL，就可以使用了！

## 🌐 其他部署选项

### Vercel 部署

Vercel 主要用于前端，但可以通过 Serverless Functions 部署：

1. 安装 Vercel CLI：
```bash
npm install -g vercel
```

2. 部署：
```bash
vercel
```

### Railway 部署

1. 访问 https://railway.app
2. 连接 GitHub 仓库
3. 自动检测并部署

### Heroku 部署

1. 安装 Heroku CLI
2. 登录：`heroku login`
3. 创建应用：`heroku create deepseek-tracker`
4. 推送：`git push heroku main`

## 📁 项目结构

```
PythonProject1/
├── app.py                  # Flask 主应用
├── balance_tracker.py      # 余额追踪逻辑
├── exchange_rate.py        # 汇率获取模块
├── main.py                 # 原始命令行脚本
├── templates/
│   ├── dashboard.html      # 主仪表板（推荐）
│   ├── index.html          # 简单查询页面
│   └── test.html           # 测试页面
├── data/
│   └── balance_history.json # 历史数据存储
├── requirements.txt        # Python 依赖
├── Procfile               # 部署配置
├── runtime.txt            # Python 版本
└── README_DEPLOY.md       # 本文件
```

## ⚙️ 环境变量（可选）

如果需要配置，在 Render 中添加环境变量：

- `PORT`：端口号（Render 自动配置）
- `FLASK_ENV`：设为 `production`

## 🔒 安全提示

1. **不要提交 API Key**：永远不要把你的 API Key 提交到 GitHub
2. **使用 .gitignore**：确保 `data/` 目录中的敏感数据不被提交
3. **HTTPS**：Render 自动提供 HTTPS，确保数据传输安全

## 📊 功能特性

- ✅ 实时汇率查询（1 小时缓存）
- ✅ USD/CNY 双币种显示
- ✅ 历史数据追踪
- ✅ 每日/每周/每月消耗统计
- ✅ 渐变色柱状图
- ✅ 平滑曲线图
- ✅ 响应式设计
- ✅ 深色主题

## 🆘 常见问题

### 部署失败？

检查：
1. `requirements.txt` 是否包含所有依赖
2. `Procfile` 是否正确
3. Python 版本是否匹配

### 数据丢失？

免费服务器可能会休眠/重启，导致本地文件丢失。解决方案：
1. 使用数据库（PostgreSQL、MongoDB）
2. 使用云存储（AWS S3、Cloudinary）
3. 定期备份 `data/balance_history.json`

### 访问速度慢？

Render 免费套餐服务器位于美国，中国访问可能较慢。可以：
1. 使用国内云服务（阿里云、腾讯云）
2. 升级到付费套餐选择更近的区域

## 📝 更新应用

修改代码后：

```bash
git add .
git commit -m "更新描述"
git push
```

Render 会自动检测 GitHub 更新并重新部署。

## 🎉 完成！

现在你的 DeepSeek 余额追踪系统已经 24/7 在线，可以随时随地访问！

访问地址：https://你的应用名.onrender.com
