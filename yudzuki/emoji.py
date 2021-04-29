from .role import Role

__all__ = (
    "Emoji"
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
        self.id = data["id"]
        self.name = data["name"]
        self.managed = data["managed"]
        self.animated = data["animated"]
        
        self.roles = data.get("roles", [])
        
    def _get_json(self):
        return self.data
    
    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name
    
    @property
    def managed(self):
        return self.managed
    
    @property
    def animated(self):
        return self.animated
    
    @property
    def roles(self):
        return [Role(v) for v in self.roles]
