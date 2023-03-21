from abc import ABC
from collections import namedtuple

from Model.abstract_model import Model
from Repositories.interfaces.interface_database_connection import IDataBaseClient


class BaseRepository(ABC):
    def __init__(self, client: IDataBaseClient, model_name: str, model: Model):
        self.client = client
        self.model_name = model_name
        self.model = model

    def save(self):
        # save change in database
        self.client.save()

    def create_one(self, object_dto: object) -> Model:
        id_label = self.model._get_model_fields()[0]
        query = self._create_query(object_dto.__dict__.keys())
        self.client.execute(query, tuple(object_dto.__dict__.values()))
        return self.find_one_by_id(self.client.cursor.lastrowid, id_label=id_label)

    def find_one_by_id(self, item_id: int, id_label='id'):
        query = self._find_one_query(id_label)
        self.client.execute(query, (item_id,))
        item = self.client.cursor.fetchone()
        print(f'este encontre: {item}')
        return self._build_object(item, self.model._get_model_fields())

    def find_all(self):
        query = self._find_all_query()
        self.client.execute(query)
        items_data = self.client.cursor.fetchall()
        items = list()
        for entry in items_data:
            items.append(self._build_object(entry, self.model._get_model_fields()))
        return items

    def find_one_and_delete(self, field_name: str, field_value: any):
        query = self._delete_query(field_name)
        self.client.execute(query, (field_name,))
        return True

    def find_one_and_update(self, field_name: str, field_value: any, object_update_dto: object):
        query = self._update_query(field_name, object_update_dto.__dict__.keys())
        self.client.execute(query, (field_value,))
        return True

    def _create_query(self, object_attributes_keys: list) -> str:
        query_fields = ''
        query_values = ''

        for field in object_attributes_keys:
            query_fields += str(field) + ', '
            query_values += '?, '


        query_fields = '(' + query_fields[0:-2] + ')'
        query_values = '(' + query_values[0:-2] + ')'
        query_operation = f'INSERT INTO {self.model_name} '

        return query_operation + query_fields + ' VALUES' + query_values + ';'

    def _update_query(self, object_id_name: str, object_dto_attributes_keys: str):
        query_fields = ''
        query_operation = f'UPDATE {self.model_name} '
        for field in object_dto_attributes_keys:
            query_fields += f'SET {field} = ?, '

        query_condition = f' WHERE {object_id_name} = ? ;'
        return query_operation + query_fields[0:-2] + query_condition

    def _delete_query(self, object_id_name: str):
        return f'DELETE FROM {self.model_name} WHERE {object_id_name} = ?;'

    def _find_one_custom_fields_query(self, object_id_name: str, object_attributes_keys: list):
        query_fields = 'SELECT '
        for field in object_attributes_keys:
            query_fields += f'{field}, '

        return query_fields[0:-2] + f' FROM {self.model_name} WHERE {object_id_name} = ?;'

    def _find_one_query(self, object_id_name: str):
        return f'SELECT * FROM {self.model_name} WHERE {object_id_name} = ?;'

    def _find_all_query(self):
        return f'SELECT * FROM {self.model_name}'

    def _build_object(self, data: tuple, object_attributes_keys: iter):
        if len(data) != len(object_attributes_keys):
            raise ValueError('passed iterables has not the same len')
        Object_tuple = namedtuple('Object_tuple', object_attributes_keys)
        object_args = Object_tuple._make(data)
        return self.model(object_args)
