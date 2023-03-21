from abc import ABC, abstractmethod


class Model(ABC):
    @staticmethod
    def _get_model_fields() -> tuple:
        raise NotImplementedError()