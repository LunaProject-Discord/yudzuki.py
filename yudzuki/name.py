import datetime

__all__ = (
    "Name",
)

class Name:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<Name name={self.name}>"
        )
    
    def _update(self, data):
        self._name = data["name"]
        self._updated_at = data["updated_at"]
        self._created_at = data["created_at"]
    
    def _get_json(self):
        return self.data
    
    @property
    def name(self):
        return self._name
    
    @property
    def updated_at(self):
        return datetime.datetime.utcfromtimestamp(self._updated_at).replace(tzinfo=datetime.timezone.utc)
    
    @property
    def created_at(self):
        return datetime.datetime.utcfromtimestamp(self._created_at).replace(tzinfo=datetime.timezone.utc)
