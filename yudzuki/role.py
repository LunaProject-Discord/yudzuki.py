__all__ = (
    "Role"
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
    
    def _update(self, data):
        self.id = data["id"]
        self.color = data["color"]
        self.managed = data["managed"]
        self.name = data["name"]
        self.guild_id = data["guild_id"]
        self.mentionable = data["mentionable"]
        self.position = data["potition"]
        self.hoisted = data["hoisted"]
    
    @property
    def id(self):
        return self.id
    
    @property
    def color(self):
        return self.color
    
    @property
    def managed(self):
        return self.managed
    
    @property
    def name(self):
        return self.name
    
    @property
    def guild_id(self):
        return self.guild_id
    
    @property
    def mentionable(self):
        return self.mentionable
    
    @property
    def position(self):
        return self.position
    
    @property
    def hoisted(self):
        return self.hoisted
