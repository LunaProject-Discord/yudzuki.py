import asyncio
import logging
import traceback

import aiohttp

from .errors import *
from .gateway import *
from .http import HTTPClient
from . import util
from .user import User
from .guild import Guild
from .name import Name
from .channel import Channel
from .emoji import Emoji
from .role import Role

__all__ = (
    "YudzukiClient",
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

    async def get_user(self, user_id: int):
        data = await self.http.get_user(user_id)
        
        return User(data)
    
    async def get_self(self):
        data = await self.http.get_self()
        
        return User(data)
    
    async def get_user_guilds(self, user_id: int):
        data = await self.http.get_user_guilds(user_id)
        
        return Guild(data)
    
    async def get_user_names(self, user_id: int):
        data = await self.http.get_user_names(user_id)
        
        return Name(data)
    
    async def reload_user(self, user_id: int):
        await self.http.reload_user(user_id)
        
    async def get_guild(self, guild_id: int):
        data = await self.http.get_guild(guild_id)
        
        return Guild(data)
    
    async def get_guild_channels(self, guild_id: int):
        data = await self.http.get_guild_channels(guild_id)
        
        return Channel(data)
    
    async def get_guild_roles(self, guild_id: int):
        data = await self.http.get_guild_roles(guild_id)
        
        return Role(data)
    
    async def get_guild_emojis(self, guild_id: int):
        data = await self.http.get_guild_emojis(guild_id)
        
        return Emoji(data)
    
    async def reload_guild(self, guild_id: int):
        await self.http.reload_guild(guild_id)
