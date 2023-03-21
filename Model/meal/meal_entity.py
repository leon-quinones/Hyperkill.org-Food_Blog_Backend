from collections import namedtuple

from Model.abstract_model import Model


class Meal(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        pass

    def __init__(self, args: namedtuple):
        self.id = int(args.id)
        self.name = args.name

