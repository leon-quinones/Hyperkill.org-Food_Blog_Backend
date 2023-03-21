from Controller.base_controller import BaseController
from Model.recipe.recipe_create_dto import RecipeCreateDto
from Repositories.base_repository import BaseRepository


class RecipeController(BaseController):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository)


    def create(self, recipe_dto: RecipeCreateDto):
        return self._repository.create_one(recipe_dto)
