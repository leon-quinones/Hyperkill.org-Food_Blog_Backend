from Controller.base_controller import BaseController
from Controller.recipe_controller import RecipeController
from typing import Union

from Model.ingredient.ingredient_entity import Ingredient
from Model.measure.meaure_entity import Measure
from Model.quantity.quantity_create_dto import QuantityCreateDto
from Model.recipe.recipe_create_dto import RecipeCreateDto
from Model.recipe.recipe_entity import Recipe
from Model.serve.serve_create_dto import ServeCreateDto
from Model.serve.serve_entity import Serve


class RecipeView:
    def __init__(self,
                 recipe_controller: Union[BaseController, RecipeController],
                 serve_controller: BaseController,
                 quantity_controller: BaseController
                 ):
        self.__serve_controller = serve_controller
        self.__recipe_controller = recipe_controller
        self.__qty_controller = quantity_controller


    def __get_text_input(self):
        text = input()
        return text

    def __get_ingredient_info(self, message: str):

        blankspace = " "
        ingredient_info = input(message).strip()
        if len(ingredient_info) == 0:
            return None, None, None
        if blankspace not in ingredient_info:
            print('Invalid format!. Try again.')
            print('Please use the following format to pass ingredients information :')
            print('quantity measure ingredient')
            self.__get_ingredient_info(message)
        information  = ingredient_info.split()
        if len(information) > 3 or len(information) < 2:
            print('Invalid format!. Try again.')
            print("Please pass correct info using the format")
            print('quantity measure ingredient')
            self.__get_ingredient_info(message)

        if len(information) == 2:
            try:
                qty = int(information[0])
                measure = None
                ingredient_name = information[1]

            except ValueError as e:
                print(ValueError)
                self.__get_ingredient_info(message)

        if len(information) == 3:
            try:
                qty = int(information[0])
                measure = information[1]
                ingredient_name = information[2]
            except ValueError as e:
                print(ValueError)
                self.__get_ingredient_info(message)

        return qty, measure, ingredient_name

    def find_element_in_iter(self, short_string: str, iterable_array: iter, message: str, field_name: str):
        if short_string == '':
            return None
        element_tuple = list()
        for i, element in enumerate(iterable_array):
            if short_string in element.__dict__.get(field_name):
                element_tuple.append(element)

        number_of_elements = len(element_tuple)
        if number_of_elements == 0 and short_string != '':
            print(f'Not {message} was found using {short_string}. '
                  f'Please add the {message} to database')
            return None
        if number_of_elements > 1:
            print(f'Number of {message} found: {number_of_elements}. '
                  f'Please select one and  try it again')
            for element in element_tuple:
                print(f'{element.__dict__.get(field_name)}', end=' ')
            return None
        return element_tuple[0]

    def found_measure(self, short_string: str, measures: iter) -> Measure:
        return self.find_element_in_iter(short_string, measures, 'measure', 'measure_name')

    def found_ingredient(self, short_string: str, ingredients: iter) -> Ingredient:
        return self.find_element_in_iter(short_string, ingredients, 'ingredient', 'ingredient_name')

    def create_recipe(self, meals: iter, ingredients: iter, measures: iter, unitless_id: int):
        add_other_recipe = True
        number_of_ingredients = 0
        print('Pass the empty recipe name to exit.')
        while add_other_recipe:
            add_other_ingredient = True
            print(f'Recipe name: ')
            recipe_name = self.__get_text_input()
            if recipe_name is None or recipe_name == '':
                print('Exit')
                return None
            print(f'Recipe description: ')
            recipe_description = self.__get_text_input()

            for i, meal in enumerate(meals):
                print(f'{i+1}) {meal.meal_name}', end=' ')
            print()
            print('When the dish can be served: (You can select one or various separated by space)')
            serve_id = self.__get_text_input().split(" ")
            recipe_created: Recipe = self.__recipe_controller.create(RecipeCreateDto(recipe_name, recipe_description))
            for mid in serve_id:
                serve_added: Serve = self.__serve_controller.create(ServeCreateDto(mid, recipe_created.recipe_id))
            print('Please enter the ingredients of your recipe')
            print('Pressing <Enter> without passing info should finish the gathering')
            print('The ingredients should be entered in the following format:')
            print('quantity measure ingredient')

            while add_other_ingredient:
                qty, measure, ingredient = self.__get_ingredient_info('Add ingredient info (quantity measure '
                                                                      'ingredient) <press enter to stop>: ')
                if qty is None and measure is None and ingredient is None:
                    add_other_ingredient = False
                    continue
                if measure is None:
                    measure_id = unitless_id
                else:
                    try:
                        measure_id = self.found_measure(measure, measures).measure_id
                    except AttributeError as e:
                        print(e)
                try:
                    ingredient_id = self.found_ingredient(ingredient, ingredients).ingredient_id
                    print(measure_id, unitless_id)
                    self.__qty_controller.create(QuantityCreateDto(measure_id, ingredient_id, qty, recipe_created.recipe_id))
                    number_of_ingredients += 1
                except AttributeError as e:
                    print(e)
            if number_of_ingredients > 0:
                self.__recipe_controller.save()
                print('Recipe was created successfully!')
            else:
                print('Invalid recipe!. Add at least one ingredient to the recipe')
                continue
            if recipe_created is None:
                add_other_recipe = False











