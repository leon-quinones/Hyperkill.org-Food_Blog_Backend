from Model.abstract_model import Model


class Ingredient(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        pass

    def __init__(self, name: str):
        self.id = None
        self.name = name