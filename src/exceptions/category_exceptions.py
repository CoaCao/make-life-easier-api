class CategoryNotFoundException(Exception):
    def __init__(self, category_id: int):
        self.category_id = category_id
