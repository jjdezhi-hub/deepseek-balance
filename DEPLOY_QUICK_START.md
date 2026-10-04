# 🚀 快速部署到 Render（5分钟完成）

## 第 1 步：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写：
   - Repository name: `deepseek-balance-tracker`
   - Description: `DeepSeek API 余额追踪系统`
   - 选择 **Public** 或 **Private**（都可以）
3. **不要**勾选 "Add a README file"
4. 点击 "Create repository"

## 第 2 步：推送代码到 GitHub

复制 GitHub 给你的命令，在本项目目录运行：

```bash
cd D:/PycharmProjects/PythonProject1

# 添加远程仓库（替换成你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/deepseek-balance-tracker.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

**提示**：如果要求登录，使用 GitHub Personal Access Token（不是密码）

## 第 3 步：部署到 Render

### 3.1 注册 Render

1. 访问 https://render.com
2. 点击 **"Get Started"**
3. 选择 **"Sign in with GitHub"**（推荐）
4. 授权 Render 访问你的 GitHub

### 3.2 创建 Web Service

1. 在 Render 仪表板，点击 **"New +"** → **"Web Service"**
2. 点击 **"Connect a repository"**
3. 找到并选择 `deepseek-balance-tracker` 仓库
4. 点击 **"Connect"**

### 3.3 配置服务

填写以下信息：

```
Name: deepseek-balance-tracker
Region: Oregon (US West) - 免费区域
Branch: main
Runtime: Python 3

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Instance Type: Free
```

**重要**：确保 Instance Type 选择 **Free** ✅

### 3.4 部署

1. 点击 **"Create Web Service"**
2. 等待 2-3 分钟（Render 会自动构建和部署）
3. 看到绿色的 **"Live"** 状态就成功了！

### 3.5 获取你的 URL

部署成功后，Render 会提供一个 URL，例如：

```
https://deepseek-balance-tracker.onrender.com
```

点击这个 URL 就可以访问你的应用了！🎉

## 🔄 后续更新

修改代码后，推送到 GitHub：

```bash
git add .
git commit -m "更新描述"
git push
```

Render 会自动检测更新并重新部署（约 1-2 分钟）。

## ⚠️ 免费套餐限制

- **自动休眠**：15 分钟无访问会休眠，下次访问需要 30-50 秒启动
- **数据持久性**：重启后 `data/balance_history.json` 会丢失
- **流量限制**：每月 100GB（个人使用足够）

### 解决数据丢失问题

**方案 1：使用 GitHub 备份**
```bash
# 定期备份数据到 GitHub
git add data/balance_history.json
git commit -m "Backup data"
git push
```

**方案 2：升级到付费套餐**
- $7/月，支持持久化存储
- 无休眠，访问更快

**方案 3：使用数据库**
- 添加 PostgreSQL（Render 免费提供）
- 修改代码从文件存储改为数据库

## 🆘 遇到问题？

### 构建失败？
- 检查 `requirements.txt` 是否正确
- 查看 Render 的构建日志

### 访问 404？
- 确认 Start Command 是 `gunicorn app:app`
- 检查 `app.py` 文件存在

### 推送 GitHub 失败？
- 使用 Personal Access Token 而不是密码
- 生成 Token：GitHub → Settings → Developer settings → Personal access tokens

## ✨ 完成！

现在你的 DeepSeek 余额追踪系统已经：
✅ 24/7 在线运行
✅ 随时随地访问
✅ 自动更新部署
✅ 完全免费使用

享受你的云端应用吧！🚀
