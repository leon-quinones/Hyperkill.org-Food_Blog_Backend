from Controller.base_controller import BaseController
from Model.meal.meal_create_dto import MealCreateDto
from Repositories.base_repository import BaseRepository


class MealController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)

    def create(self, meal_create_dto: MealCreateDto):
        return self._repository.create_one(meal_create_dto)

    def get_all(self):
        return self._repository.find_all()
