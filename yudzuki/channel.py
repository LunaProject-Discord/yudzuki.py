__all__ = (
    "TextChannel",
    "VoiceChannel",
    "StoreChannel",
    "CategoryChannel",
    "Channel"
)

class TextChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
class VoiceChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
class StoreChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
class CategoryChannel:
        
    def __init__(self, data):
        self.data = data
        self._update(data)
    
class Channel:
    
    def __init__(self, data):
        self.data = data
        
