from collections import namedtuple

from Model.abstract_model import Model


class Recipe(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('id', 'name', 'description')
        return class_fields

    def __init__(self, args: namedtuple):
        self.id = int(args.id)
        self.name = args.name
        self.description = args.description



