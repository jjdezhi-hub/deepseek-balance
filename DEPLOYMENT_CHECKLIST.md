## ✅ 部署前检查清单

在推送到 GitHub 和部署之前，请确认以下事项：

### 📋 文件检查

- [x] `app.py` - Flask 主应用
- [x] `balance_tracker.py` - 余额追踪逻辑
- [x] `exchange_rate.py` - 汇率获取模块
- [x] `requirements.txt` - Python 依赖列表
- [x] `Procfile` - Render 部署配置
- [x] `runtime.txt` - Python 版本指定
- [x] `.gitignore` - Git 忽略文件配置
- [x] `README.md` - 项目说明文档
- [x] `templates/dashboard.html` - 主界面
- [x] `templates/index.html` - 简单查询页面
- [x] `templates/test.html` - 测试页面

### 🔒 安全检查

- [x] 敏感数据已添加到 `.gitignore`
- [x] `data/balance_history.json` 不会被提交
- [x] 代码中没有硬编码的 API Key
- [ ] **你的操作**：不要在 GitHub 上暴露你的 DeepSeek API Key

### 🚀 准备部署

#### 步骤 1：推送到 GitHub

```bash
# 替换成你的 GitHub 用户名和仓库名
git remote add origin https://github.com/你的用户名/deepseek-balance-tracker.git
git branch -M main
git push -u origin main
```

**提示**：
- 如果提示输入密码，使用 Personal Access Token 而不是密码
- 生成 Token：GitHub → Settings → Developer settings → Personal access tokens → Generate new token
- 权限选择：`repo`（完整仓库访问）

#### 步骤 2：部署到 Render

1. **访问** https://render.com
2. **注册/登录**（建议用 GitHub 账号）
3. **创建服务**：New + → Web Service
4. **连接仓库**：选择你的 `deepseek-balance-tracker` 仓库
5. **配置**：
   ```
   Name: deepseek-balance-tracker
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free ✅
   ```
6. **部署**：点击 "Create Web Service"
7. **等待**：2-3 分钟
8. **完成**：获得你的 URL（例如 https://deepseek-balance-tracker.onrender.com）

### 📝 部署后验证

部署成功后，测试以下功能：

- [ ] 打开应用 URL，页面正常加载
- [ ] 实时汇率显示正确
- [ ] 输入 API Key 能成功查询余额
- [ ] USD 转 CNY 金额正确
- [ ] 柱状图和曲线图正常显示
- [ ] 切换每日/每周/每月正常工作
- [ ] 切换 CNY/USD 货币正常

### 🎯 下一步

- 分享你的应用 URL 给团队
- 添加书签到浏览器
- 定期查询余额以建立历史数据
- 考虑升级到付费套餐以获得数据持久化

### 🔧 故障排除

#### 构建失败？
```bash
# 检查 requirements.txt
cat requirements.txt

# 确保包含：
Flask==3.0.0
Werkzeug==3.0.1
gunicorn==21.2.0
```

#### 应用无法启动？
```bash
# 检查 Procfile
cat Procfile

# 确保内容为：
web: gunicorn app:app
```

#### 页面 404？
- 确认 `app.py` 文件存在
- 检查 Render 日志中的错误信息
- 确认路由配置正确

### 📞 需要帮助？

- 查看 `README_DEPLOY.md` 详细文档
- 查看 Render 部署日志
- 检查 GitHub Actions（如果配置了 CI/CD）

---

**准备好了？开始部署吧！** 🚀

按照 `DEPLOY_QUICK_START.md` 中的步骤，5 分钟内完成部署！
