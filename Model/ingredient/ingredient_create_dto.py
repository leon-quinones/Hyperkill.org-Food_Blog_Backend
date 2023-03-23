class IngredientCreateDto:
    def __init__(self, ingredient_id: int, name: str):
        self.ingredient_id = ingredient_id
        self.ingredient_name = name
