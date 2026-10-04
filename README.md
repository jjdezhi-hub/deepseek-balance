# 💎 DeepSeek 余额追踪系统

一个美观、强大的 DeepSeek API 余额监控和可视化工具，支持实时汇率转换和消耗分析。

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## ✨ 功能特性

### 💱 实时汇率
- 自动获取最新 USD/CNY 汇率
- 1 小时智能缓存
- 支持手动刷新
- 多数据源备份

### 📊 数据可视化
- **渐变柱状图**：直观展示每日/每周/每月消耗
- **平滑曲线图**：追踪余额变化趋势
- **交互式图表**：悬停查看详细数据

### 💰 余额追踪
- 自动记录第一次查询为基准
- 计算总消耗金额
- 显示剩余余额
- USD/CNY 双币种显示

### 🎨 现代界面
- 深色主题设计
- 响应式布局（支持手机/平板/电脑）
- 流畅动画效果
- 渐变色配色方案

## 🚀 快速开始

### 本地运行

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/deepseek-balance-tracker.git
cd deepseek-balance-tracker

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行应用
python app.py

# 4. 访问应用
# 打开浏览器访问 http://127.0.0.1:5000
```

### 云端部署

详见 [快速部署指南](DEPLOY_QUICK_START.md)

## 📸 界面预览

### 主仪表板
- 实时汇率显示
- 三大统计卡片（当前余额、初始余额、总消耗）
- 双图表展示（消耗趋势 + 余额变化）
- 时间周期切换（每日/每周/每月）

### 功能演示
1. 输入 DeepSeek API Key
2. 点击查询余额
3. 自动转换为人民币
4. 生成可视化图表
5. 切换不同时间维度查看数据

## 🛠️ 技术栈

- **后端**：Python 3.11 + Flask 3.0
- **前端**：HTML5 + CSS3 + Vanilla JavaScript
- **图表**：Chart.js 4.4.0
- **部署**：Gunicorn + Render
- **存储**：JSON 文件（支持扩展为数据库）

## 📁 项目结构

```
deepseek-balance-tracker/
├── app.py                      # Flask 主应用
├── balance_tracker.py          # 余额追踪核心逻辑
├── exchange_rate.py            # 汇率获取模块
├── main.py                     # 原始命令行脚本
├── requirements.txt            # Python 依赖
├── Procfile                    # 部署配置
├── runtime.txt                 # Python 版本指定
├── .gitignore                  # Git 忽略文件
├── README.md                   # 项目说明（本文件）
├── README_DEPLOY.md            # 详细部署文档
├── DEPLOY_QUICK_START.md       # 快速部署指南
├── templates/
│   ├── dashboard.html          # 主仪表板页面
│   ├── index.html              # 简单查询页面
│   └── test.html               # 调试测试页面
└── data/
    └── balance_history.json    # 历史数据（自动生成）
```

## 🔌 API 端点

### POST `/api/query`
查询余额并保存历史记录

**请求**：
```json
{
  "api_key": "sk-xxx"
}
```

**响应**：
```json
{
  "success": true,
  "balance_usd": 18.05,
  "balance_cny": 121.30,
  "exchange_rate": 6.72
}
```

### GET `/api/stats`
获取统计数据（当前、基准、消耗、历史）

**响应**：
```json
{
  "success": true,
  "data": {
    "current": {...},
    "baseline": {...},
    "total_consumed_usd": 1.95,
    "total_consumed_cny": 13.10,
    "daily": [...],
    "weekly": [...],
    "monthly": [...]
  }
}
```

### GET `/api/exchange-rate`
获取当前汇率

**响应**：
```json
{
  "success": true,
  "rate": 6.72,
  "updated_at": "2024-10-04T11:30:00Z",
  "cached": true
}
```

### POST `/api/refresh-rate`
强制刷新汇率（忽略缓存）

## 🎯 使用场景

- ✅ 监控 DeepSeek API 使用情况
- ✅ 分析 AI 项目成本
- ✅ 预测未来消耗趋势
- ✅ 多项目余额对比
- ✅ 团队共享余额监控

## 🔒 安全建议

1. **不要泄露 API Key**：永远不要将 API Key 提交到公开仓库
2. **使用环境变量**：生产环境建议用环境变量存储敏感信息
3. **定期备份数据**：定期备份 `data/balance_history.json`
4. **HTTPS 访问**：云端部署自动启用 HTTPS

## 📈 未来计划

- [ ] 支持多个 API Key 管理
- [ ] 添加消耗预警（余额不足提醒）
- [ ] 导出数据（CSV/Excel）
- [ ] 数据库存储（PostgreSQL/SQLite）
- [ ] 用户认证系统
- [ ] 多语言支持（英文/中文切换）
- [ ] 移动端 App
- [ ] Telegram/微信通知

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 自由使用和修改

## 👨‍💻 作者

由 Claude Fable 5 协助开发

## 🙏 致谢

- [DeepSeek API](https://platform.deepseek.com/) - 提供强大的 AI 服务
- [Chart.js](https://www.chartjs.org/) - 优秀的图表库
- [Flask](https://flask.palletsprojects.com/) - 轻量级 Web 框架
- [Render](https://render.com/) - 免费云端部署平台

---

⭐ 如果觉得有用，请给个 Star！
