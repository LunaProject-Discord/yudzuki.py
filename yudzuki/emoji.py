from .role import Role

__all__ = (
    "Emoji",
)

class Emoji:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
        
    def __repr__(self):
        return (
            f"<Emoji name={self.name} id={self.id}>"
        )
    
    def _update(self, data):
        self._id = data["id"]
        self._name = data["name"]
        self._managed = data["managed"]
        self._animated = data["animated"]
        
        self._roles = data.get("roles", [])
        
    def _get_json(self):
        return self.data
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def managed(self):
        return self._managed
    
    @property
    def animated(self):
        return self._animated
    
    @property
    def roles(self):
        return [Role(v) for v in self._roles]
