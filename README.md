## ST-MCP-Server

[[https://static.699pic.com/baiduAiPlugin/logo.png]()]

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

图片搜索，视频搜索，音乐搜索

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

    - code (int): 状态码
    
    - msg (string): 错误信息
    
    - data (array): 搜索结果
    
        - title (string): 图片标题
    
        - pic_type (int): 图片类型
    
        - extension_name (string): 图片格式
    
        - detail_preview_src (string): 图片地址
    
        - href (string): 图片链接
    
    - count (int): 总条数，用于分页

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

    - code (int): 状态码
    
    - msg (string): 错误信息
    
    - data (array): 搜索结果
    
        - title (string): 视频标题
    
        - cate (int): 视频类型
    
        - extension_name (string): 视频格式
    
        - detail_preview_src (string): 视频地址
    
        - href (string): 视频链接
    
    - count (int): 总条数，用于分页

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

    - code (int): 状态码
    
    - msg (string): 错误信息
    
    - data (array): 搜索结果
    
        - title (string): 音乐标题
    
        - cover (int): 音乐封面
    
        - detail_preview_src (string): 音乐地址
    
        - href (string): 音乐链接
    
    - count (int): 总条数，用于分页

#### 最容易被唤起的 Prompt 示例

"搜索背景音乐"、"查找30秒以内的音效"、"搜索2分钟以上的配乐"

## 可适配平台

可以使用 cline, cursor, claude desktop 或支持MCP server调用的的其他终端

## 服务开通链接

[待补充]

## 鉴权方式

API Key 认证

- 获取方式：通过摄图网申请

- 使用方式：在请求头中添加 `X-API-KEY` 和 `X-API-TOKEN`

## 安装部署

### 系统依赖

- 安装 Python 3.12 或者更高版本
- 安装 uv
  - 如果是linux系统
    
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  - 如果是window系统
    
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
- 同步依赖项并更uv.lock:
  
  ```bash
  uv sync
  ```
- 构建cmp server:
  
  ```bash
  uv build
  ```

### 使用 Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

On Windows: `%APPDATA%/Claude/claude_desktop_config.json`



server configuration

```json
{
  "mcpServers": {
    "mongo_mcp_server": {
      "disabled": false,
      "command": "uv",
      "args": [
        "--directory",
        "/<path to mcp-servers>/mcp-server/",
        "run",
        "main.py"
      ],
      "env": {
        "API_KEY": "your-access-key-id",
        "API_SECRET": "your-access-key-secret"
      },
      "transportType": "stdio"
    }
  }
}

```

## License

   MIT License