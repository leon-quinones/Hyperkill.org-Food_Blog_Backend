from Controller.base_controller import BaseController
from Controller.recipe_controller import RecipeController
from typing import Union

from Model.recipe.recipe_create_dto import RecipeCreateDto


class RecipeView:
    def __init__(self, controller: Union[BaseController, RecipeController]):
        self.__controller = controller


    def __get_text_input(self):
        text = input()
        return text

    def create_recipe(self):
        add_other_recipe = True
        print('Pass the empty recipe name to exit.')
        while add_other_recipe:
            print(f'Recipe name: ')
            recipe_name = self.__get_text_input()
            if recipe_name is None or recipe_name == '':
                print('Exit')
                return None
            print(f'Recipe description: ')
            recipe_description = self.__get_text_input()
            recipe_created = self.__controller.create(RecipeCreateDto(recipe_name, recipe_description))
            self.__controller.save()
            print('Recipe was created successfully!')
            if recipe_created is None:
                add_other_recipe = False









