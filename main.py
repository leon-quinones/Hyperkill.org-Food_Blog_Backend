import os
import sqlite3

from dotenv import load_dotenv
from sqlite3 import OperationalError

from Controller.ingredient_controller import IngredientController
from Controller.measure_controller import MeasureController
from Controller.quantity_controller import QuantityController
from Controller.recipe_controller import RecipeController
from Controller.serve_controller import ServeController
from Controller.meal_controller import MealController
from Repositories.ingredient_repository import IngredientRepository
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.meal_repository import MealRepository
from Repositories.measure_repository import MeasureRepository
from Repositories.quantity_repository import QuantityRepository
from Repositories.recipe_repository import RecipeRepository
from Repositories.serve_repository import ServeRepository
from View.recipes.recipes_view import RecipeView


class SqliteClient(IDataBaseClient):
    def __init__(self, connection_string: str):
        self.cursor = None
        self.conn = None
        self.connect(connection_string)
        # sqlite3 insert sqlite_sequence table
        if len(self.__retrieve_tables_in_database()) - 1 != self.__get_number_of_models():
            self.__build_database_tables()
            self.__populate_database()

    def __build_database_tables(self):
        for i, query in enumerate(self.__database_table_building_queries()):
            try:
                self.cursor.execute(query)
                self.conn.commit()
                print(f'Query #{i + 1} succeed, continue with next one')
            except OperationalError as e:
                print(f'Query #{i + 1} failed, skipping')
                print(e)

    def __database_table_building_queries(self):
        meal_query = 'CREATE TABLE IF NOT EXISTS meals ( ' \
                     'meal_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                     'meal_name TEXT UNIQUE NOT NULL' \
                     ');'

        ingredient_query = 'CREATE TABLE IF NOT EXISTS ingredients ( ' \
                           'ingredient_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                           'ingredient_name TEXT UNIQUE NOT NULL' \
                           ');'

        measure_query = 'CREATE TABLE IF NOT EXISTS measures ( ' \
                        'measure_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                        'measure_name TEXT UNIQUE' \
                        ');'

        recipe_query = 'CREATE TABLE IF NOT EXISTS recipes ( ' \
                       'recipe_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                       'recipe_name TEXT NOT NULL, ' \
                       'recipe_description TEXT' \
                       ');'

        serve_query = 'CREATE TABLE IF NOT EXISTS serve ( ' \
                      'serve_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                      'meal_id INTEGER NOT NULL, ' \
                      'recipe_id INTEGER NOT NULL, ' \
                      'CONSTRAINT fk_meal FOREIGN KEY (meal_id) REFERENCES meals(meal_id), ' \
                      'CONSTRAINT fk_recipe FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ' \
                      ');'

        quantity_query = 'CREATE TABLE IF NOT EXISTS quantity (' \
                         'quantity_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' \
                         'measure_id INTEGER NOT NULL, ' \
                         'ingredient_id INTEGER NOT NULL,' \
                         'quantity INTEGER NOT NULL, ' \
                         'recipe_id INTEGER NOT NULL, ' \
                         'CONSTRAINT fk_measure FOREIGN KEY (measure_id) REFERENCES measures(measure_id), ' \
                         'CONSTRAINT fk_ingredient FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id), ' \
                         'CONSTRAINT fk_recipe FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ' \
                         ');'

        return [meal_query, ingredient_query, measure_query, recipe_query, serve_query, quantity_query]

    def __get_number_of_models(self):
        return 6

    def __populate_database(self):
        data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
                "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
                "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
        keys = data.keys()
        for key in keys:
            for value in data[key]:
                insert_query = f'INSERT INTO "{key}" ("{key[0:-1]}_name") VALUES ("{value}");'
                print(insert_query)
                self.cursor.execute(insert_query)
                self.conn.commit()

    def __retrieve_tables_in_database(self):
        try:
            self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
            tables = self.cursor.fetchall()
            return tables
        except OperationalError:
            print('Cannot retrieve tables from database')

    def connect(self, connection_string):
        try:
            self.conn = sqlite3.connect(connection_string, timeout=240)
            self.cursor = self.conn.cursor()
            print('SQLITE3 connection succeed')
        except OperationalError:
            print('Cannot connect to database')

    def disconnect(self):
        self.conn.close()
        print('Disconnected from database')

    def save(self):
        self.conn.commit()

    def execute(self, query: str, query_args: tuple):
        self.cursor.execute(query, query_args)


class App:
    def __init__(self):

        self.data_base_connection = SqliteClient(os.getenv('DATABASE_HOST'))
        self.repository = RecipeRepository(self.data_base_connection)
        self.serve_repository = ServeRepository(self.data_base_connection)
        self.meal_repository = MealRepository(self.data_base_connection)
        self.measure_repository = MeasureRepository(self.data_base_connection)
        self.quantity_repository = QuantityRepository(self.data_base_connection)
        self.ingredient_repository = IngredientRepository(self.data_base_connection)
        self.controller = RecipeController(self.repository)
        self.serve_controller = ServeController(self.serve_repository)
        self.meal_controller = MealController(self.meal_repository)
        self.measure_controller = MeasureController(self.measure_repository)
        self.ingredient_controller = IngredientController(self.ingredient_repository)
        self.quantity_controller = QuantityController(self.quantity_repository)
        self.view = RecipeView(self.controller, self.serve_controller, self.quantity_controller)

    def __build_repositories(self):
        pass

    def create_recipes(self):
        meals = self.meal_controller.get_all()
        ingredients = self.ingredient_controller.get_all()
        measures = self.measure_controller.get_all()
        unitless_id = self.measure_controller.get_by_unit_name('').measure_id
        self.view.create_recipe(meals, ingredients, measures, unitless_id)


if __name__ == '__main__':
    load_dotenv()
    app = App()
    app.create_recipes()
