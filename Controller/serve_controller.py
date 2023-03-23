from Controller.base_controller import BaseController
from Model.serve.serve_create_dto import ServeCreateDto
from Repositories.base_repository import BaseRepository


class ServeController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)


    def create(self, serve_create_dto: ServeCreateDto):
        return self._repository.create_one(serve_create_dto)

    def get_all(self):
        return self._repository.find_all()