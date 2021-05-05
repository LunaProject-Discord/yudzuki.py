__all__ = (
    "Role",
)

class Role:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def _get_json(self):
        return self.data

    def __repr__(self):
        return (
            f"<Role id={self.id} name={self.name}>"
        )
    
    def __str__(self):
        return (
            f"{self.name}"
        )
    
    def _update(self, data):
        self._id = data["id"]
        self._color = data["color"]
        self._managed = data["managed"]
        self._name = data["name"]
        self._guild_id = data["guild_id"]
        self._mentionable = data["mentionable"]
        self._position = data["potition"]
        self._hoisted = data["hoisted"]
    
    @property
    def id(self):
        return self._id
    
    @property
    def color(self):
        return self._color
    
    @property
    def managed(self):
        return self._managed
    
    @property
    def name(self):
        return self._name
    
    @property
    def guild_id(self):
        return self._guild_id
    
    @property
    def mentionable(self):
        return self._mentionable
    
    @property
    def position(self):
        return self._position
    
    @property
    def hoisted(self):
        return self._hoisted
