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
    
    def __str__(self):
        return (
            f"{self.name}"
        )
    
    def _update(self, data):
        self._name = data["name"]
        self._updated_at = int(data["updated_at"])
        self._created_at = int(data["created_at"])
    
    def _get_json(self):
        return self.data
    
    @property
    def name(self):
        return self._name
    
    @property
    def updated_at(self):
        return self._updated_at
    
    @property
    def created_at(self):
        return self._created_at
