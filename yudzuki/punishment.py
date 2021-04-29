__all__ = (
    "Punishment",
)

class Punishment:
    
    def __init__(self, data):
        self.data = data
        self._update(data)
    
    def _update(self, data):
        self.mute_dic = data.get("mute", {})
        self.kick_dic = data.get("kick", {})
        self.local_ban_dic = data.get("local_ban", {})
        self.global_ban_dic = data.get("global_ban", {})
    
    def _get_json(self):
        return self.data
    
    def _get_mute(self):
        return self.mute_dic
    
    def _get_kick(self):
        return self.kick_dic
    
    def _get_ban(self):
        return self.local_ban_dic
    
    def _get_ban(self):
        return self.ban_dic
