from Model.ingredient.ingredient_entity import Ingredient
from Repositories.base_repository import BaseRepository
from Repositories.interfaces.interface_database_connection import IDataBaseClient


class MealRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient, model_name: str):
        self.super().__init__(database_connection, model_name, Ingredient)