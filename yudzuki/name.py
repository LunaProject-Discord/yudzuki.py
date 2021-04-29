import datetime

__all__ = (
    "Name"
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
        self.name = data["name"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
    
    @property
    def name(self):
        return self.name
    
    @property
    def updated_at(self):
        return datetime.datetime.utcfromtimestamp(self.updated_at).replace(tzinfo=datetime.timezone.utc)
    
    @property
    def created_at(self):
        return datetime.datetime.utcfromtimestamp(self.created_at).replace(tzinfo=datetime.timezone.utc)
