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
            f"<UserSetting permission={self.permission} evaluate_value={self.evaluate_value} verified={self.verified}>"
            f" timezone={self.timezone} language={self.language}>"
        )
    
    def _update(self, data):
        self._verified = data["verified"]
        self._permission = data["permission"]
        self._language = data["language"]
        self._evaluate_value = data["evaluate_value"]
        self._timezone = data["timezone"]
    
    @property
    def permission(self):
        return self._permission
    
    @property
    def staff(self):
        return staff_value(self._permission)
    
    @property
    def evaluate_value(self):
        return self._evaluate_value
    
    @property
    def verified(self):
        return self._verified
    
    @property
    def language(self):
        return self._language
    
    @property
    def timezone(self):
        return self._timezone
    
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
        self._verified = data["verified"]
        self._language = data["language"]
        self._prefix = data["prefix"]
        self._timezone = data["timezone"]
    
    @property
    def verified(self):
        return self._verified
    
    @property
    def language(self):
        return self._language
    
    @property
    def prefix(self):
        return self._prefix
    
    @property
    def timezone(self):
        return self._timezone
