from enum import Enum

class AuthEnums(Enum):
    CREATED = "created",
    OKAY = "okay",
    ERROR = "error",
    FAILED = "failed"
    EXIST = "exist"
    NONE_FOUND = "None found"
    ACCECC_NOT_GRANTED = "access not granted"
    
    INVALID_PHONE_NUMBER = "invalid phone number"