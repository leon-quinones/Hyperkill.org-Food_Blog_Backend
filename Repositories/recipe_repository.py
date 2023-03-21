from Model.recipe.recipe_entity import Recipe
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.base_repository import BaseRepository


class RecipeRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient):
        super().__init__(database_connection, 'recipes', Recipe)

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



