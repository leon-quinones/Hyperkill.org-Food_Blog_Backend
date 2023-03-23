from Controller.base_controller import BaseController
from Model.quantity.quantity_create_dto import QuantityCreateDto
from Repositories.base_repository import BaseRepository


class QuantityController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)


    def create(self, quantity_dto: QuantityCreateDto):
        return self._repository.create_one(quantity_dto)

    def get_all(self):
        return self._repository.find_all()