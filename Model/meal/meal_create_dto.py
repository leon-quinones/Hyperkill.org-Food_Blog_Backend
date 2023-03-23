from collections import namedtuple

from Model.abstract_model import Model


class MealCreateDto(Model):
    def __init__(self, name: str):
        self.name = name