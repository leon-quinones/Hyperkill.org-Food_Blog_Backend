from Model.recipe.recipe_entity import Recipe
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.base_repository import BaseRepository


class RecipeRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient):
        super().__init__(database_connection, 'recipes', Recipe)

    def find_recipe_by_ingredients_and_meal(self, ingredients: iter, meals: iter):
        meals_elements = '(' + ''.join(['?, '] * len(meals))[0:-2] + ')'
        ingredients_elements = '(' + ''.join(['?, '] * len(ingredients))[0:-2] + ')'
        number_of_ingredients = len(ingredients)

        query = 'SELECT q.recipe_id, recipe_name, recipe_description, i.ingredient_name FROM ( ' \
                'SELECT r.recipe_id, recipe_name, recipe_description FROM recipes as r ' \
                'INNER JOIN serve as s ON s.recipe_id = r.recipe_id ' \
                'INNER JOIN (' \
                f'SELECT * FROM meals WHERE meal_name IN {meals_elements} ' \
                ') as m ON s.meal_id = m.meal_id' \
                ') as rmax ' \
                'INNER JOIN quantity as q ON q.recipe_id = rmax.recipe_id ' \
                'INNER JOIN ( ' \
                f'SELECT * FROM ingredients WHERE ingredient_name IN {ingredients_elements} ' \
                ') as i ON q.ingredient_id = i.ingredient_id ' \
                f'GROUP BY q.recipe_id HAVING COUNT() = {number_of_ingredients}'

        print(query, tuple(meals), tuple(ingredients))
        self.client.execute(query, (*meals, *ingredients))
        recipes = self.client.cursor.fetchall()
        print(recipes)
        return [self._build_object(item, self.model._get_model_fields()) for item in recipes]

    # def create_one(self, recipe_dto: RecipeCreateDto):
    #     query = self._create_query(recipe_dto.__dict__.keys())
    #     self.client.execute(query, tuple(recipe_dto.__dict__.values()))
    #     return True
    #
    # def save(self):
    #     self.client.save()
    #
    # def find_one_by_id(self, item_id: int, id_label='id'):
    #     query = self._find_one_query(id_label)
    #     self.client.execute(query, (item_id, ))
    #     item = self.client.cursor.fetchone()
    #     return self._build_object(item, self.model._get_model_fields())
    #
    # def find_all(self):
    #     query = self._find_all_query()
    #     self.client.execute(query)
    #     items_data = self.client.cursor.fetchall()
    #     items = list()
    #     for entry in items_data:
    #         items.append(self._build_object(entry, self.model._get_model_fields()))
    #     return items
    #
    # def find_one_and_delete(self, field_name: str, field_value: any):
    #     query = self._delete_query(field_name)
    #     self.client.execute(query, (field_name, ))
    #     return True
    #
    # def find_one_and_update(self, field_name: str, field_value: any, object_update_dto: object):
    #     query = self._update_query(field_name, object_update_dto.__dict__.keys())
    #     self.client.execute(query, (field_value, ))
    #     return True



