from abc import ABC

from Repositories.base_repository import BaseRepository


class BaseController(ABC):
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def create(self):
        pass

    def save(self):
        self._repository.save()


