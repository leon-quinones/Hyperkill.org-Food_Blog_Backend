class RecipeCreateDto:
    def __init__(self, name: str, description: str):
        self.recipe_name = name
        self.recipe_description = description
