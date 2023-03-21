from Model.abstract_model import Model


class Recipe(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('id', 'name', 'description')
        return class_fields

    def __init__(self, recipe_id: int, name: str, description: str):
        self.id = recipe_id
        self.name = name
        self.description = description



