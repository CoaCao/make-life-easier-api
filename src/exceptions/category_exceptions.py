class CategoryNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class CategoryExistException(Exception):
    def __init__(self, message: str):
        self.message = message
