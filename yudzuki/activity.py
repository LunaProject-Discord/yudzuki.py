import datetime

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
    
    def _get_json(self):
        return self.data
    
    def _update(self, data):
        self.start = data.get("start", 0)
        self.end = data.get("end", 0)
        
    @property
    def start(self):
        return datetime.datetime.utcfromtimestamp(self.start).replace(tzinfo=datetime.timezone.utc)
    
    @property
    def end(self):
        return datetime.datetime.utcfromtimestamp(self.end).replace(tzinfo=datetime.timezone.utc)

class Activity:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def __repr__(self):
        return (
            f"<Activity type={self.type}>"
        )
    
    def _get_json(self):
        return self.data
    
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
