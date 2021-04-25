import asyncio
import logging
import traceback

import aiohttp

from .errors import *
from .gateway import *
from .http import HTTPClient
from . import util
from .user import User

__all__ = (
    "YudzukiClient"
)

log = logging.getLogger(__name__)

class YudzukiClient:
    
    def __init__(self, token):
        self.token = token
        
        self._closed = False
        
        self.http = HTTPClient(token)
    
    async def close(self):
        if self._closed:
            return
        
        await self.http.close()
