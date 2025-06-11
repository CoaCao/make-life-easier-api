class ProductNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message