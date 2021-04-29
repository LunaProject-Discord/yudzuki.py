from .emoji import Emoji
from .channel import Channel
from .role import Role
from .setting import GuildSetting

__all__ = (
    "Guild",
)

class Guild:

    def __init__(self, data):
        self._data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<Guild id={self.id} name={self.name!r}>"
        )
    
    def __str__(self):
        return f"{self.name}#{self.discriminator}"
    
    def _update(self, data):
        self._id = data["id"]
        self._name = data["name"]
        self._roles = data["roles"]
        self._features = data["features"]
        self._splash = data["splash"]
        self._channels = data["channels"]
        self._emojis = data["emojis"]
        self._boost_tier = data["boost_tier"]
        self._boost_count = data["boost_count"]
        self._region = data["region"]
        self._icon = data["icon"]
        self._icon_url = data["icon_url"]
        self._description = data["description"]
        self._locale = data["locale"]
        self._afk_timeout = data["afk_timeout"]
        self._splash_url = data["splash_url"]
        self._banner_url = data["banner_url"]
        self._vanity_url = data["vanity_url"]
        self._settings = data["settings"]
        self._banner = data["banner"]
        self._verification_level = data["verification_level"]
        self._default_notification_level = data["default_notification_level"]
        self._vanity_code = data["vanity_code"]
        self._mfa_level = data["mfa_level"]
        self._explicit_content_level = data["explicit_content_level"]
                        
    def _get_json(self):
        return self.data
                      
    @property
    def settings(self):
        return GuildSetting(self._settings)

    @property
    def roles(self):
        return [Role(v) for v in self._roles]

    @property
    def channels(self):
        return [Channel(v) for v in self._channels]

    @property
    def emojis(self):
        return [Emoji(v) for v in self._emojis]                 
                         
    @property
    def boost_tier(self):
        return self._boost_tier

    @property
    def description(self):
        return self._description

    @property
    def locale(self):
        return self._locale

    @property
    def afk_timeout(self):
        return self._afk_timeout

    @property
    def splash_url(self):
        return self._splash_url

    @property
    def banner_url(self):
        return self._banner_url
                         
    @property
    def vanity_url(self):
        return self._vanity_url

    @property
    def banner(self):
        return self._banner

    @property
    def verification_level(self):
        return self._verification_level
    
    @property
    def default_notification_level(self):
        return self._default_notification_level

    @property
    def vanity_code(self):
        return self._vanity_code

    @property
    def mfa_level(self):
        return self._mfa_level

    @property
    def explicit_content_level(self):
        return self._explicit_content_level

    @property
    def region(self):
        return self._region

    @property
    def splash(self):
        return self._splash

    @property
    def boost_count(self):
        return self._boost_count
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def permissions(self):
        return self._permissions
   
    @property
    def icon_url(self):
        return self._icon_url
    
    @property
    def icon(self):
        return self._icon
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def features(self):
        return self._features
