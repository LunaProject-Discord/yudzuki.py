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
        self.id = data["id"]
        self.name = data["name"]
        self.roles = data["roles"]
        self.features = data["features"]
        self.splash = data["splash"]
        self.channels = data["channels"]
        self.emojis = data["emojis"]
        self.boost_tier = data["boost_tier"]
        self.boost_count = data["boost_count"]
        self.region = data["region"]
        self.icon = data["icon"]
        self.icon_url = data["icon_url"]
        self.description = data["description"]
        self.locale = data["locale"]
        self.afk_timeout = data["afk_timeout"]
        self.splash_url = data["splash_url"]
        self.banner_url = data["banner_url"]
        self.vanity_url = data["vanity_url"]
        self.settings = data["settings"]
        self.banner = data["banner"]
        self.verification_level = data["verification_level"]
        self.default_notification_level = data["default_notification_level"]
        self.vanity_code = data["vanity_code"]
        self.mfa_level = data["mfa_level"]
        self.explicit_content_level = data["explicit_content_level"]
                        
    def _get_json(self):
        return self.data
                       
    @property
    def _get_data(self):
        return self.data

    @property
    def settings(self):
        return GuildSetting(self.settings)

    @property
    def roles(self):
        return [Role(v) for v in self.roles]

    @property
    def channels(self):
        return [Channel(v) for v in self.channels]

    @property
    def emojis(self):
        return [Emoji(v) for v in self.emojis]                 
                         
    @property
    def boost_tier(self):
        return self.boost_tier

    @property
    def description(self):
        return self.description

    @property
    def locale(self):
        return self.locale

    @property
    def afk_timeout(self):
        return self.afk_timeout

    @property
    def splash_url(self):
        return self.splash_url

    @property
    def banner_url(self):
        return self.banner_url
                         
    @property
    def vanity_url(self):
        return self.vanity_url

    @property
    def banner(self):
        return self.banner

    @property
    def verification_level(self):
        return self.verification_level
    
    @property
    def default_notification_level(self):
        return self.default_notification_level

    @property
    def vanity_code(self):
        return self.vanity_code

    @property
    def mfa_level(self):
        return self.mfa_level

    @property
    def explicit_content_level(self):
        return self.explicit_content_level

    @property
    def region(self):
        return self.region

    @property
    def splash(self):
        return self.splash

    @property
    def boost_count(self):
        return self.boost_count
    
    @property
    def owner(self):
        return self.owner
    
    @property
    def permissions(self):
        return self.permissions
   
    @property
    def icon_url(self):
        return self.icon_url
    
    @property
    def icon(self):
        return self.icon
    
    @property
    def name(self):
        return self.name
    
    @property
    def id(self):
        return self.id
    
    @property
    def features(self):
        return self.features
