from typing import Union

from Controller.base_controller import BaseController
from Model.recipe.recipe_create_dto import RecipeCreateDto
from Repositories.base_repository import BaseRepository
from Repositories.recipe_repository import RecipeRepository


class RecipeController(BaseController):
    def __init__(self, repository: Union[BaseRepository, RecipeRepository]):
        super().__init__(repository)


    def create(self, recipe_dto: RecipeCreateDto):
        return self._repository.create_one(recipe_dto)

    def get_all(self):
        return self._repository.find_all()

    def get_recipes_by_ingredients_and_meal(self, ingredients: iter, meals: iter):
        return self._repository.find_recipe_by_ingredients_and_meal(ingredients, meals)
