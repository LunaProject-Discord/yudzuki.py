__all__ = (
    "HTTPException",
    "Forbidden",
    "APINotFound",
    "YudzukiException",
    "NotFound",
    "YudzukiServerError",
    "UnauthorizedDetected"
)

class YudzukiException(Exception):
    pass

class APINotFound(YudzukiException):
    
    def __init__(self):
        msg = "The api to connect to YudzukiAPI was not found."
        
        super().__init__(msg)

class UnauthorizedDetected(YudzukiException):
    pass

class HTTPException(YudzukiException):
    
    def __init__(self, resp, msg):
        self.resp = resp
        self.status = resp.status
        self.text = msg
        
        super().__init__(f"{self.status}: {self.text}")

class Forbidden(HTTPException):
    pass
    
class NotFound(HTTPException):
    pass
    
class YudzukiServerError(HTTPException):
    pass
