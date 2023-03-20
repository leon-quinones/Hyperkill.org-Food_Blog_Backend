from abc import ABC, abstractmethod
from Repositories.interface_database_connection import IDataBaseClient


class IRepository(ABC):
    def __init__(self, client: IDataBaseClient, model_name: str):
        self.client = client
        self.model = model_name

    @abstractmethod
    def save(self):
        # save change in database
        raise NotImplementedError

    @abstractmethod
    def create_one(self):
        # save change in database
        raise NotImplementedError

    @abstractmethod
    def find_one_by_id(self, item_id: int):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_one_and_delete(self, field_name: str, field_value: any):
        raise NotImplementedError

    @abstractmethod
    def find_one_and_update(self, field_name: str, field_value: any, item_update_dto: any):
        raise NotImplementedError

    def _create_query(self, object_attributes_keys: list) -> str:
        query_fields = ''
        query_values = ''

        for field in object_attributes_keys:
            print(field, query_values)
            query_fields += str(field) + ', '
            query_values += '?, '
            print(query_values)

        query_fields = '(' + query_fields[0:-2] + ')'
        query_values = '(' + query_values[0:-2] + ')'
        query_operation = f'INSERT INTO {self.model_name} '

        return query_operation + query_fields + ' VALUES ' + query_values + ';'

    def _update_query(self, object_id_name: str, object_dto_attributes_keys: str):
        query_fields = ''
        query_operation = f'UPDATE {self.model_name} '
        for field in object_dto_attributes_keys:
            query_fields += f'SET {field} = ?, '

        query_condition = f' WHERE {object_id_name} = ?;'
        return query_operation + query_fields[0:-2] + query_condition

    def _delete_query(self, object_id_name: str):
        return f'DELETE FROM {self.model_name} WHERE {object_id_name} = ?;'
