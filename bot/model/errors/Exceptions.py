class WrongUsernameOrPasswordException(Exception):
    def __init__(self, details: str):
        self.details = details


class ServerError(Exception):
    def __init__(self, details: str):
        self.details = details
