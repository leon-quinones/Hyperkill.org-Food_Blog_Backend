from collections import namedtuple

from Model.abstract_model import Model


class Serve(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('serve_id', 'meal_id', 'recipe_id')
        return class_fields

    def __init__(self, args: namedtuple):
        self.serve_id = int(args.serve_id)
        self.meal_id = args.meal_id
        self.recipe_id = args.recipe_id
