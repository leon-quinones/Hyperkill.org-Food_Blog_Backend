from Controller.base_controller import BaseController
from Model.measure.measure_create_dto import MeasureCreateDto
from Repositories.base_repository import BaseRepository


class MeasureController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)


    def create(self, measure_dto: MeasureCreateDto):
        return self._repository.create_one(measure_dto)

    def get_all(self):
        return self._repository.find_all()

    def get_by_unit_name(self, unit_value: str):
        return self._repository.find_one_by_field(unit_value, 'measure_name')
