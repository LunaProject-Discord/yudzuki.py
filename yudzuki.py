import aiohttp
import json

from urllib.parse import quote as _uriquote

async def json_or_text(response):
    text = await response.text(encoding='utf-8')
    
    try:
        if response.headers['content-type'] == 'application/json':
            return json.loads(text)
    except KeyError:
        pass

    return text

class HTTPException(Exception):
    
    def __init__(self, resp, msg):
        self.resp = resp
        self.status = resp.status
        
        self.text = msg
        
        super().__init__(f"{self.status}: {self.text}")

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

class YudzukiClient:
    
    def __init__(self, bot, token):
        self.bot = bot
        self.yudzuki_token = token
        self.session = aiohttp.ClientSession(headers={"Authorization": f"Bearer {token}", "User-Agent":"Midori YudzukiAPIClient"})
        
    async def request(self, route):
        try:
            async with self.session.request(route.method, route.url) as ret:
                data = await json_or_text(ret)
                
                if 300 > ret.status >= 200:
                    return data
                
                if ret.status == 429:
                    raise HTTPException(ret, data)
                
                if ret.status in {500, 502}:
                    raise HTTPException(ret, data)
                
                if ret.status == 403:
                    raise HTTPException(ret, data)
                elif ret.status == 404:
                    raise HTTPException(ret, data)
                elif ret.status == 503:
                    raise HTTPException(ret, data)
                else:
                    raise HTTPException(ret, data)
        except Exception as e:
            raise Exception(e)
    
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