import aiohttp
import logging

from urllib.parse import quote as _uriquote

from .errors import HTTPException, Forbidden, APINotFound, NotFound, YudzukiServerError, UnauthorizedDetected
from .gateway import YudzukiClientWebSocketResponse
from .util import json_or_text
from .__init__ import __version__

log = logging.getLogger(__name__)

class Route:
    
    BASE = "https://api.aoichaan0513.jp/v1"
    
    def __init__(self, method, path, **parameters):
        self.path = path
        self.method = method
        url = self.BASE + self.path
        
        if parameters:
            self.url = url.format_map({k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        else:
            self.url = url

class HTTPClient:
    
    def __init__(self, token):
        if token is None:
            raise UnauthorizedDetected("YudzukiAPI token not provided")
            
        self.token = token
        self.session = None
        
        user_agent = "YudzukiClient (https://github.com/LunaProject-Discord/yudzuki.py {0}) aiohttp/{1}"
        self.user_agent = user_agent.format(__version__, aiohttp.__version__)
        
        self.recreate()
    
    def recreate(self):
        if not self.session:
            self.session = aiohttp.ClientSession(
                ws_response_class=YudzukiClientWebSocketResponse
            )
        
        if self.session.closed:
            self.session = aiohttp.ClientSession(
                ws_response_class=YudzukiClientWebSocketResponse
            )
        
    async def request(self, route):
        method = route.method
        url = route.url
        
        headers = {
            "User-Agent": self.user_agent,
        }
        
        if self.token is not None:
            headers["Authorization"] = "Bearer " + self.token
    
        try:
            async with self.session.request(method, url) as ret:
                log.debug("%s %s has returned %s", method, url, ret.status)
            
                data = await json_or_text(ret)
                
                if 300 > ret.status >= 200:
                    log.debug("%s %s has received %s", method, url, data)
                    return data
                
                format = "We are being rate limited."
                
                if ret.status == 429:
                    log.warning(format)
                    raise HTTPException(ret, data)
                
                if ret.status == 400:
                    raise HTTPException(ret, data)
                elif ret.status == 401:
                    raise HTTPException(ret, data)
                elif ret.status == 403:
                    raise Forbidden(ret, data)
                elif ret.status == 404:
                    raise NotFound(ret, data)
                elif ret.status == (500, 502, 503):
                    raise YudzukiServerError(ret, data)
                else:
                    raise HTTPException(ret, data)
                    
        except OSError as e:
            raise
    
    async def close(self):
        if self.session:
            await self.session.close()
    
    def get_user(self, user_id):
        return self.request(Route("GET", "/users/{user_id}", user_id=user_id))
    
    def get_self(self):
        return self.request(Route("GET", "/users/@me"))
    
    def get_user_guilds(self, user_id):
        return self.request(Route("GET", "/users/{user_id}/guilds", user_id=user_id))
    
    def get_user_names(self, user_id):
        return self.request(Route("GET", "/users/{user_id}/names", user_id=user_id))
    
    def reload_user(self, user_id):
        return self.request(Route("PATCH", "/users/{user_id}", user_id=user_id))
    
    def get_guild(self, guild_id):
        return self.request(Route("GET", "/guilds/{guild_id}", guild_id=guild_id))
    
    def get_guild_channels(self, guild_id):
        return self.request(Route("GET", "/guilds/{guild_id}/channels", guild_id=guild_id))
    
    def get_guild_roles(self, guild_id):
        return self.request(Route("GET", "/guilds/{guild_id}/roles", guild_id=guild_id))
    
    def get_guild_emojis(self, guild_id):
        return self.request(Route("GET", "/guilds/{guild_id}/emojis", guild_id=guild_id))
    
    def reload_guild(self, guild_id):
        return self.request(Route("PATCH", "/guilds/{guild_id}", guild_id=guild_id))
