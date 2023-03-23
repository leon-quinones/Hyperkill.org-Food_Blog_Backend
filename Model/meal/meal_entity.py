from collections import namedtuple

from Model.abstract_model import Model


class Meal(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('meal_id', 'meal_name')
        return class_fields

    def __init__(self, args: namedtuple):
        self.meal_id = int(args.meal_id)
        self.meal_name = args.meal_name

