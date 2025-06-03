MMCP Server 产品名称：ST-MCP-Server
[![产品Logo]([https://static.699pic.com/baiduAiPlugin/logo.png])]
## 版本信息
v1.0.0
## 产品描述
### 短描述
摄图网多媒体内容搜索服务，提供图片、视频、音乐等多媒体资源的智能搜索能力。
### 长描述
ST-MCP-Server 是摄图网提供的多媒体内容搜索服务，集成了图片、视频、音乐等多种媒体资源的搜索功能。通过丰富的筛选条件和智能排序，帮助用户快速找到所需的媒体资源，支持多种格式和类型的资源检索。
## 分类
多媒体搜索、内容检索
## 标签
图片搜索，视频搜索，音乐搜索，媒体资源
## Tools
本 MCP Server 产品提供以下 Tools(工具/能力):
### Tool1: 图片搜索
#### 详细描述
提供图片资源的智能搜索服务，支持多种筛选条件，包括图片类型、比例、人物特征等，帮助用户精准找到所需图片资源。
#### 调试所需的输入参数:
输入：
    - kw（string）：搜索关键词
    - order（int）：排序方式（1：推荐, 2：最新）
    - has_avatar（int）：肖像权（0：全部 1：有 2：无）
    - is_prime（int）：精品（0：全部 1：是 2：否）
    - extension_name（string）：图片格式
    - direction（int）：比例（0：竖版 1：横版 2：全部）
    - pic_type（int）：图片类型（0:all 1：照片 2：创意背景 3：插画 4：设计模板 5：办公文档 7：免抠元素 9：gif）
    - num（int）：人数（4：全部）
    - sex（int）：性别（0：全部 1：男 2：女）
    - race（int）：人种（0：全部 1：黄色 2：白色 3：黑色 4：棕色）
    - page（int）：页码
    - size（int）：每页显示数量
输出：
    - APIResponse：包含搜索结果的响应对象
#### 最容易被唤起的 Prompt 示例
"搜索自然风景图片"、"查找商务人物照片"、"搜索创意插画"
### Tool2: 视频搜索
#### 详细描述
提供视频资源的智能搜索服务，支持按类别、分辨率、比例等条件筛选，帮助用户快速找到合适的视频素材。
#### 调试所需的输入参数:
输入：
    - kw（string）：搜索关键词
    - order（int）：排序方式（1：推荐, 2：最新）
    - cate（int）：视频类别（0：全部 18：实拍 98：AE模板 227：背景视频 338：pr模板 351：会声会影 363：视频元素 449：edius 460：视频海报）
    - video_rate（int）：视频分辨率（0：全部 1：720p 2：1080p 3：4k 4：8k）
    - video_scale（int）：视频比例（0-所有 1-2:1 2-16:9 3-3:2 4-4:3 5-1:1 6-3:4 7-2:3 8-9:16 9-1:2 10-2.39:1 255-其它）
    - page（int）：页码
    - size（int）：每页显示数量
输出：
    - APIResponse：包含搜索结果的响应对象
#### 最容易被唤起的 Prompt 示例
"搜索4K风景视频"、"查找16:9比例的视频素材"、"搜索AE模板"
### Tool3: 音乐搜索
#### 详细描述
提供音乐资源的智能搜索服务，支持按时长等条件筛选，帮助用户找到合适的音乐素材。
#### 调试所需的输入参数:
输入：
    - kw（string）：搜索关键词
    - order（int）：排序方式（1：推荐, 2：最新）
    - duration（int）：时长（0：全部 1：30秒以下 2：30-60s 3：60s-2m 4：2-3m 5：3m及以上）
    - page（int）：页码
    - size（int）：每页显示数量
输出：
    - APIResponse：包含搜索结果的响应对象
#### 最容易被唤起的 Prompt 示例
"搜索背景音乐"、"查找30秒以内的音效"、"搜索2分钟以上的配乐"
## 可适配平台
Python, Node.js, Java, Cursor
## 服务开通链接
[待补充]
## 鉴权方式
API Key 认证
- 获取方式：通过摄图网管理后台申请
- 使用方式：在请求头中添加 `X-API-KEY` 和 `X-API-SECRET`
## 安装部署
### 客户部署服务
1. 克隆代码仓库
```bash
git clone https://github.com/your-org/st-mcp-server.git
```
2. 安装依赖
```bash
pip install -r requirements.txt
```
3. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入以下配置：
# API_BASE_URL=https://api.699pic.com/v1/AiPlugin
# API_KEY=你的API密钥
# API_SECRET=你的API密钥
# LOG_LEVEL=INFO
```
4. 启动服务
```bash
python main.py
```
### 客户提供代码
本服务支持代码部署，客户可以获取源代码并根据需求进行定制化开发。
### 客户要求我方部署
支持私有化部署，具体部署方案和权责边界需要单独沟通确定。
## 资源列表 - optional
## 商业化 - optional
## 产品截图/视频 - optional
## 支持协议
- 提供 7x24 小时技术支持
- 问题响应时间：2小时内
- 支持方式：邮件、工单系统
## License
MIT License