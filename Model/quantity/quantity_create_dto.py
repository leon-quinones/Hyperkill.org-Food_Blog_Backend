class QuantityCreateDto:
    def __init__(self, measure_id: int, ingredient_id: int, qty: int, recipe_id: int):
        self.measure_id = measure_id
        self.ingredient_id = ingredient_id
        self.quantity = qty
        self.recipe_id = recipe_id
