from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
from typing import Dict, Any, Optional
import logging
from pydantic import BaseModel, Field
import time
import hmac
import hashlib
# 加载环境变量
load_dotenv()

# 初始化服务器
mcp = FastMCP("st_server")

# 配置日志
logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API配置
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.699pic.com/v1/AiPlugin")
API_KEY = os.getenv("API_KEY", "")
API_SECRET = os.getenv("API_SECRET", "")

class APIResponse(BaseModel):
    """API响应模型"""
    code: int
    msg: str
    data: list = Field(default_factory=list)
    count: Optional[int] = None

async def api_request(endpoint: str, data: Dict[str, Any]) -> APIResponse:
    """发送API请求到摄图网
    
    Args:
        endpoint: API端点
        data: 请求数据
        
    Returns:
        APIResponse: API响应对象
        
    Raises:
        Exception: 当API请求失败时抛出异常
    """
    url = f"{API_BASE_URL}{endpoint}"

    params = dict(data)
    params["x-api-key"] = API_KEY
    timestamp = str(int(time.time()))
    params["x-api-timestamp"] = timestamp

    sorted_items = sorted(params.items())
    sign_str = '&'.join(f"{k}={v}" for k, v in sorted_items)

    token = hmac.new(API_SECRET.encode(), sign_str.encode(), hashlib.sha256).hexdigest()

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY,
        "X-API-TOKEN": token,
        "X-API-TIMESTAMP": timestamp,
        "X-API-TYPE" : "hmac"
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()
            return APIResponse(**response.json())
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP错误: {e}")
        return APIResponse(code=0, msg=f"HTTP错误: {e}")
    except httpx.RequestError as e:
        logger.error(f"请求错误: {e}")
        return APIResponse(code=0, msg=f"请求错误: {e}")
    except Exception as e:
        logger.error(f"未知错误: {e}")
        return APIResponse(code=0, msg=f"未知错误: {e}")

@mcp.tool()  
async def search_image(
    kw: str,
    order: int = Field(1, description="排序 (1：推荐, 2：最新)"),
    has_avatar: int = Field(0, description="肖像权 (0：全部 1：有 2：无)"),
    is_prime: int = Field(0, description="精品 (0：全部 1：是 2：否)"),
    extension_name: str = Field("", description="格式"),
    direction: int = Field(2, description="比例 (0：竖版 1：横版 2：全部)"),
    pic_type: int = Field(0, description="图片类型 (0:all 1：照片 2：创意背景 3：插画 4：设计模板 5：办公文档 7：免抠元素 9：gif)"),
    num: int = Field(4, description="人数 (4：全部)"),
    sex: int = Field(0, description="性别 (0：全部 1：男 2：女)"),
    race: int = Field(0, description="人种 (0：全部 1：黄色；2：白色；3：黑色：4：棕色)"),
    page: int = Field(1, description="页码"),
    size: int = Field(20, description="一页显示多少条")
) -> APIResponse:
    """图片搜索
    
    Args:
        kw: 搜索词
        order: 排序方式
        has_avatar: 肖像权
        is_prime: 精品
        extension_name: 格式
        direction: 比例
        pic_type: 图片类型
        num: 人数
        sex: 性别
        race: 人种
        page: 页码
        size: 每页数量
        
    Returns:
        APIResponse: 搜索结果
    """
    data = {
        "kw": kw,
        "order": order,
        "has_avatar": has_avatar,
        "is_prime": is_prime,
        "extension_name": extension_name,
        "direction": direction,
        "pic_type": pic_type,
        "num": num,
        "sex": sex,
        "race": race,
        "page": page,
        "size": size
    }
    
    logger.info(f"搜索图片: {kw}")
    return await api_request("/search_image", data)

@mcp.tool()
async def search_media(
    kw: str,
    order: int = Field(1, description="排序 (1：推荐, 2：最新)"),
    cate: int = Field(0, description="分类 视频类别 (0：全部;18：实拍;98：AE模板;227：背景视频;338：pr模板;351：会声会影;363：视频元素;449：edius;460：视频海报)"),
    video_rate: int = Field(0, description="视频分辨率 (0：全部1：720p 2：1080p 3：4k 4：8k)"),
    video_scale: int = Field(0, description="视频比例 (0-所有;1-2:1;2-16:9;3-3:2;4-4:3;5-1:1;6-3:4;7-2:3;8-9:16;9-1:2;10-2.39:1;255-其它)"),
    page: int = Field(1, description="页码"),
    size: int = Field(20, description="一页显示多少条")
) -> APIResponse:
    """视频搜索
    
    Args:
        kw: 搜索词
        order: 排序方式
        cate: 视频类别
        video_rate: 视频分辨率
        video_scale: 视频比例
        page: 页码
        size: 每页数量
        
    Returns:
        APIResponse: 搜索结果
    """
    data = {
        "kw": kw,
        "order": order,
        "cate": cate,
        "video_rate": video_rate,
        "video_scale": video_scale,
        "page": page,
        "size": size
    }
    
    logger.info(f"搜索视频: {kw}")
    return await api_request("/search_media", data)

@mcp.tool()
async def search_music(
    kw: str,
    order: int = Field(1, description="排序 (1：推荐, 2：最新)"),
    duration: int = Field(0, description="时长 (0：全部 1：30秒以下 2：30-60s 3：60s-2m 4：2-3m 5：3m及以上)"),
    page: int = Field(1, description="页码"),
    size: int = Field(20, description="一页显示多少条")
) -> APIResponse:
    """音乐搜索
    
    Args:
        kw: 搜索词
        order: 排序方式
        duration: 时长
        page: 页码
        size: 每页数量
        
    Returns:
        APIResponse: 搜索结果
    """
    data = {
        "kw": kw,
        "order": order,
        "duration": duration,
        "page": page,
        "size": size
    }
    
    logger.info(f"搜索音乐: {kw}")
    return await api_request("/search_music", data)

if __name__ == "__main__":
    mcp.run(transport="stdio")
