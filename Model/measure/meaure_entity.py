from collections import namedtuple

from Model.abstract_model import Model


class Measure(Model):
    @staticmethod
    def _get_model_fields() -> tuple:
        class_fields = ('measure_id', 'measure_name')
        return class_fields

    def __init__(self, args: namedtuple):
        self.measure_id = args.measure_id
        self.measure_name = args.measure_name
