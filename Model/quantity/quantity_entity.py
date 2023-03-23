from collections import namedtuple

from Model.abstract_model import Model


class Quantity(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('quantity_id', 'measure_id', 'ingredient_id', 'quantity', 'recipe_id')
        return class_fields

    def __init__(self, args: namedtuple):
        self.quantity_id = int(args.quantity_id)
        self.measure_id = args.measure_id
        self.ingredient_id = args.ingredient_id
        self.quantity = args.quantity
        self.recipe_id = args.recipe_id
