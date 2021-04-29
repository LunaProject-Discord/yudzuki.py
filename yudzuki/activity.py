__all__ = (
    "Activity",
    "Timestamps"
)

class Timestamps:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<Timestamps start={self.start} end={self.end}>"
        )
    
    def _update(self, data):
        self.start = data.get("start", 0)
        self.end = data.get("end", 0)
        
    @property
    def start(self):
        return self.start
    
    @property
    def end(self):
        return self.end

class Activity:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<Activity type={self.type}>"
        )
    
    def _update(self, data):
        self.name = data.get("name", "")
        self.emoji = data.get("emoji", "")
        self.url = data.get("url", "")
        self.type = data.get("type", "")
        self.timestamps = data.get("timestamps", {})
    
    @property
    def name(self):
        return self.name
    
    @property
    def emoji(self):
        return self.emoji
    
    @property
    def url(self):
        return self.url
    
    @property
    def type(self):
        return self.type
    
    @property
    def timestamps(self):
        return Timestamps(self.timestamps)
