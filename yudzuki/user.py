from .activity import Activity
from .punishment import Punishment
from .name import Name
from .setting import UserSetting

__all__ = (
    "User",
)

class User:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
        
    def __repr__(self):
        return (
            f"<User id={self.id} name={self.name!r} discriminator={self.discriminator!r}"
            f" bot={self.bot} system={self.system}>"
        )
    
    def __str__(self):
        return f"{self.name}#{self.discriminator}"
    
    def _update(self, data):
        self.name = data["name"]
        self.id = int(data["id"])
        self.discriminator = data["discriminator"]
        self.avatar = data["avatar"]
        self.settings = data["settings"]
        self.names = data["names"]
        self.punishments = data["punishments"]
        self.system = data["system"]
        self.bot = data["bot"]
        
        self.public_flags = data.get("flags", 0)
        self.avatar_url = data.get("avatar_url", None)
        self.status = data.get("online_status", "offline")
        self.activities = data.get("activities", None)
    
    def _get_json(self):
        return self.data
    
    @property
    def settings(self):
        return UserSetting(self.settings)
    
    @property
    def names(self):
        return [Name(v) for v in self.names]
    
    @property
    def status(self):
        return self.status
    
    @property
    def activities(self):
        if not self.activities:
            return None
        
        return [Activity(v) for v in self.activities]

    @property
    def public_flags(self):
        return self.public_flags
    
    @property
    def avatar(self):
        return self.avatar
    
    @property
    def avatar_url(self):
        return self.avatar_url
    
    @property
    def name(self):
        return self.name
    
    @property
    def id(self):
        return self.id
    
    @property
    def discriminator(self):
        return self.discriminator
    
    @property
    def bot(self):
        return self.bot
    
    @property
    def system(self):
        return self.system
