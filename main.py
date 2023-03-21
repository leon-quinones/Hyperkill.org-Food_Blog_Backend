import os
import sqlite3

from dotenv import load_dotenv
from sqlite3 import OperationalError

from Controller.recipe_controller import RecipeController
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.recipe_repository import RecipeRepository
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
            except OperationalError:
                print(f'Query #{i + 1} failed, skipping')

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

        return [meal_query, ingredient_query, measure_query, recipe_query]

    def __get_number_of_models(self):
        return 4

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
        self.controller = RecipeController(self.repository)
        self.view = RecipeView(self.controller)

    def __build_repositories(self):
        pass

    def create_recipes(self):
        self.view.create_recipe()




if __name__ == '__main__':
    load_dotenv()
    app = App()
    app.create_recipes()