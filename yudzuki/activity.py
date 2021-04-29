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
        self._start = data.get("start", 0)
        self._end = data.get("end", 0)
        
    @property
    def start(self):
        return datetime.datetime.utcfromtimestamp(self._start).replace(tzinfo=datetime.timezone.utc)
    
    @property
    def end(self):
        return datetime.datetime.utcfromtimestamp(self._end).replace(tzinfo=datetime.timezone.utc)

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
        self._name = data.get("name", "")
        self._emoji = data.get("emoji", "")
        self._url = data.get("url", "")
        self._type = data.get("type", "")
        self._timestamps = data.get("timestamps", {})
    
    @property
    def name(self):
        return self._name
    
    @property
    def emoji(self):
        return self._emoji
    
    @property
    def url(self):
        return self._url
    
    @property
    def type(self):
        return self._type
    
    @property
    def timestamps(self):
        return Timestamps(self._timestamps)
