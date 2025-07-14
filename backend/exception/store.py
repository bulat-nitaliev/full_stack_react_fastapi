class TypeExistsException(Exception):
    detail = "the type already exists"


class DeviceNotFoundException(Exception):
    detail = "Device not found"


class UserNotCorrectPasswordException(Exception):
    detail = "User not correct password"
