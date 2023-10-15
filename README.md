# b23.tv-tools

Flask App to generate/parse b23.tv links. 用于生成/解析 b23.tv 的 Flask 应用。

## 部署

Fork 本仓库，默认设置部署到 Vercel。

## API

### `/get?url=长链接`

从`*.bilibili.com/*`链接生成`b23.tv`短链接。

### `/parse?url=短链接`

从`b23.tv`短链接获取清洗过的长链接。

## 致谢

https://github.com/Cesium01/b23tvGenerator

https://github.com/willbe03/b23-remover-telegram-bot
