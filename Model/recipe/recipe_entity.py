from collections import namedtuple

from Model.abstract_model import Model


class Recipe(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('recipe_id', 'recipe_name', 'recipe_description')
        return class_fields

    def __init__(self, args: namedtuple):
        self.recipe_id = int(args.recipe_id)
        self.recipe_name = args.recipe_name
        self.recipe_description = args.recipe_description



