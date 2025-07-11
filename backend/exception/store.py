class TypeExistsException(Exception):
    detail = "the type already exists"


class UserNotFoundException(Exception):
    detail = "User not found"


class UserNotCorrectPasswordException(Exception):
    detail = "User not correct password"
