class UserExistsException(Exception):
    detail = 'the user already exists'

class UserNotFoundException(Exception):
    detail = 'User not found'


class UserNotCorrectPasswordException(Exception):
    detail = 'User not correct password'