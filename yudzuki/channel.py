__all__ = (
    "TextChannel",
    "VoiceChannel",
    "StoreChannel",
    "CategoryChannel",
    "Channel"
)

class TextChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<TextChannel id={self.id} name={self.name} position={self.position} nsfw={self.nsfw}"
            f" news={self.is_news} category_id={self.parent_id}>"
        )
    
    def __str__(self):
        return self.name
    
    def _get_json(self):
        return self.data
    
    def _update(self, data):
        self.id = data["id"]
        self.nsfw = data["nsfw"]
        self.guild_id = data["guild_id"]
        self.name = data["name"]
        self.position = data["position"]
        self.type = data["type"]
        self.announce = data["announce"]
        
        self.parent_id = data.get("parent_id", None)
        self.topic = data.get("topic", None)
        self.slowmode = data.get("slowmode", 0)
    
    @property
    def id(self):
        return self.id
    
    @property
    def nsfw(self):
        return self.nsfw
    
    @property
    def guild_id(self):
        return self.guild_id
    
    @property
    def name(self):
        return self.name
    
    @property
    def position(self):
        return self.position
    
    @property
    def type(self):
        return self.type
    
    @property
    def get_type(self):
        if self.announce:
            return "news"
        
        return "text"
    
    @property
    def announce(self):
        return self.announce
    
    @property
    def parent_id(self):
        return self.parent_id
    
    @property
    def topic(self):
        return self.topic
    
    @property
    def slowmode(self):
        return self.slowmode
    
class VoiceChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<VoiceChannel id={self.id} name={self.name} position={self.position}"
            f" bitrate={self.bitrate} user_limit={self.user_limit} category_id={self.parent_id}>"
        )
    
    def _get_json(self):
        return self.data
    
    def __str__(self):
        return self.name
    
    def _update(self, data):
        self.id = data["id"]
        self.guild_id = data["guild_id"]
        self.name = data["name"]
        self.position = data["position"]
        self.type = data["type"]
        self.bitrate = data["bitrate"]
        self.user_limit = data["user_limit"]
        
        self.parent_id = data.get("parent_id", None)
    
    @property
    def id(self):
        return self.id
    
    @property
    def guild_id(self):
        return self.guild_id
    
    @property
    def name(self):
        return self.name
    
    @property
    def position(self):
        return self.position
    
    @property
    def type(self):
        return self.type
    
    @property
    def get_type(self):
        return "voice"
    
    @property
    def bitrate(self):
        return self.bitrate
    
    @property
    def user_limit(self):
        return self.user_limit
    
    @property
    def parent_id(self):
        return self.parent_id
    
class StoreChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
class CategoryChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<CategoryChannel id={self.id} name={self.name} position={self.position}"
            f" nsfw={self.nsfw}>"
        )
    
    def _get_json(self):
        return self.data
    
    def __str__(self):
        return self.name
    
    def _update(self, data):
        self.id = data["id"]
        self.guild_id = data["guild_id"]
        self.position = data["position"]
        self.type = data["type"]
        self.name = data["name"]
        
        self.parent_id = data.get("parent_id", None)
        
    @property
    def id(self):
        return self.id
    
    @property
    def guild_id(self):
        return self.guild_id
    
    @property
    def position(self):
        return self.position
    
    @property
    def type(self):
        return self.type
    
    @property
    def get_type(self):
        return "category"
    
    @property
    def name(self):
        return self.name
    
    @property
    def parent_id(self):
        return self.parent_id
        
class Channel:
    
    def __init__(self, data):
        self.data = data
        
        if data["type"] == 0:
            self = TextChannel(data)
        elif data["type"] == 4:
            self = CategoryChannel(data)
        elif data["type"] == 6:
            self = StoreChannel(data)
        elif data["type"] == 2:
            self = VoiceChannel(data)
    
    def __str__(self):
        return self.data["name"]
    
    def __repr__(self):
        return f"<Channel id={self.data['id']} name={self.data['name']} guild_id={self.data['guild_id']} type={self.data['type']}>"
