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
        self._name = data["name"]
        self._id = int(data["id"])
        self._discriminator = data["discriminator"]
        self._avatar = data["avatar"]
        self._settings = data["settings"]
        self._names = data["names"]
        self._punishments = data["punishments"]
        self._system = data["system"]
        self._bot = data["bot"]
        
        self.public_flags = data.get("flags", 0)
        self.avatar_url = data.get("avatar_url", None)
        self.status = data.get("online_status", "offline")
        self.activities = data.get("activities", None)
    
    def _get_json(self):
        return self.data
    
    @property
    def settings(self):
        return UserSetting(self._settings)
    
    @property
    def names(self):
        return [Name(v) for v in self._names]
    
    @property
    def status(self):
        return self._status
    
    @property
    def activities(self):
        if not self._activities:
            return None
        
        return [Activity(v) for v in self._activities]

    @property
    def public_flags(self):
        return self._public_flags
    
    @property
    def avatar(self):
        return self._avatar
    
    @property
    def avatar_url(self):
        return self._avatar_url
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def discriminator(self):
        return self._discriminator
    
    @property
    def bot(self):
        return self._bot
    
    @property
    def system(self):
        return self._system
