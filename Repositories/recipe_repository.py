from Model.recipe.recipe_create_dto import RecipeCreateDto
from Repositories.interface_database_connection import IDataBaseClient
from Repositories.interface_repository import IRepository


class RecipeRepository(IRepository):

    def __init__(self, database_connection: IDataBaseClient, model_name: str):
        # model_name is table in database
        self.model_name = model_name
        self.database_connection = database_connection

    def create_one(self, recipe_dto: RecipeCreateDto):
        field_list = recipe_dto.__dict__
        pass

    def save(self):
        pass

    def find_one_by_id(self, item_id: int):
        pass

    def find_all(self):
        pass

    def find_one_and_delete(self, field_name: str, field_value: any):
        pass

    def find_one_and_update(self, field_name: str, field_value: any, item_update_dto: any):
        pass