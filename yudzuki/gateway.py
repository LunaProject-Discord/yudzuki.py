import aiohttp

__all__ = (
    "YudzukiClientWebSocketResponse"
)

class YudzukiClientWebSocketResponse(aiohttp.ClientWebSocketResponse):
    async def close(self, *, code: int = 4000, message: bytes = b'') -> bool:
        return await super().close(code=code, message=message)