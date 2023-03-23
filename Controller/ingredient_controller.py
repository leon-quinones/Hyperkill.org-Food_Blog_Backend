from Controller.base_controller import BaseController
from Model.ingredient.ingredient_create_dto import IngredientCreateDto
from Repositories.base_repository import BaseRepository


class IngredientController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)


    def create(self, ingredient_dto: IngredientCreateDto):
        return self._repository.create_one(ingredient_dto)

    def get_all(self):
        return self._repository.find_all()