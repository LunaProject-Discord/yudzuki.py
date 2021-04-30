__all__ = (
    "TextChannel",
    "VoiceChannel",
    "StoreChannel",
    "CategoryChannel",
    "Channel"
)

class Channel:
    
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return self.data["name"]
    
    def __repr__(self):
        return f"<Channel id={self.data['id']} name={self.data['name']} guild_id={self.data['guild_id']} type={self.data['type']}>"

class TextChannel(Channel):
        
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
        self._id = data["id"]
        self._nsfw = data["nsfw"]
        self._guild_id = data["guild_id"]
        self._name = data["name"]
        self._position = data["position"]
        self._type = data["type"]
        self._announce = data["announce"]
        
        self._parent_id = data.get("parent_id", None)
        self._topic = data.get("topic", None)
        self._slowmode = data.get("slowmode", 0)
    
    @property
    def id(self):
        return self._id
    
    @property
    def nsfw(self):
        return self._nsfw
    
    @property
    def guild_id(self):
        return self._guild_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    @property
    def type(self):
        return self._type
    
    @property
    def get_type(self):
        if self._announce:
            return "news"
        
        return "text"
    
    @property
    def announce(self):
        return self._announce
    
    @property
    def parent_id(self):
        return self._parent_id
    
    @property
    def topic(self):
        return self._topic
    
    @property
    def slowmode(self):
        return self._slowmode
    
class VoiceChannel(Channel):
        
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
        self._id = data["id"]
        self._guild_id = data["guild_id"]
        self._name = data["name"]
        self._position = data["position"]
        self._type = data["type"]
        self._bitrate = data["bitrate"]
        self._user_limit = data["user_limit"]
        
        self._parent_id = data.get("parent_id", None)
    
    @property
    def id(self):
        return self._id
    
    @property
    def guild_id(self):
        return self._guild_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    @property
    def type(self):
        return self._type
    
    @property
    def get_type(self):
        return "voice"
    
    @property
    def bitrate(self):
        return self._bitrate
    
    @property
    def user_limit(self):
        return self._user_limit
    
    @property
    def parent_id(self):
        return self._parent_id
    
class StoreChannel(Channel):
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<StoreChannel id=-- name=-->"
        )
    
    def __str__(self):
        return "None"
    
    def _update(self, data):
        pass
    
class CategoryChannel(Channel):
        
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
        self._id = data["id"]
        self._guild_id = data["guild_id"]
        self._position = data["position"]
        self._type = data["type"]
        self._name = data["name"]
        
        self._parent_id = data.get("parent_id", None)
        
    @property
    def id(self):
        return self._id
    
    @property
    def guild_id(self):
        return self._guild_id
    
    @property
    def position(self):
        return self._position
    
    @property
    def type(self):
        return self._type
    
    @property
    def get_type(self):
        return "category"
    
    @property
    def name(self):
        return self._name
    
    @property
    def parent_id(self):
        return self._parent_id
