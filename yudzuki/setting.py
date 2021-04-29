from .util import staff_value

__all__ = (
    "UserSetting",
    "GuildSetting"
)

class UserSetting:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
        
    def _get_json(self):
        return self.data

    def __repr__(self):
        return (
            f"<UserSetting permission={self.permission} evaluate_value={self.evaluate_value} verified={self.vetified}>"
            f" timezone={self.timezone} language={self.language}>"
        )
    
    def _update(self, data):
        self.verified = data["verified"]
        self.permission = data["permission"]
        self.language = data["language"]
        self.evaluate_value = data["evaluate_value"]
        self.timezone = data["timezone"]
    
    @property
    def permission(self):
        return self.permission
    
    @property
    def staff(self):
        return staff_value(self.permission)
    
    @property
    def evaluate_value(self):
        return self.evaluate_value
    
    @property
    def verified(self):
        return self.verified
    
    @property
    def language(self):
        return self.language
    
    @property
    def timezone(self):
        return self.timezone
    
class GuildSetting:
    
    def __init__(self, data):
        self.data = data
        self._update(data)

    def __repr__(self):
        return (
            f"<GuildSetting verified={self.vetified} timezone={self.timezone}>"
            f" language={self.language} prefix={self.prefix}>"
        )
    
    def _get_json(self):
        return self.data

    def _update(self, data):
        self.verified = data["verified"]
        self.language = data["language"]
        self.prefix = data["prefix"]
        self.timezone = data["timezone"]
    
    @property
    def verified(self):
        return self.verified
    
    @property
    def language(self):
        return self.language
    
    @property
    def prefix(self):
        return self.prefix
    
    @property
    def timezone(self):
        return self.timezone
