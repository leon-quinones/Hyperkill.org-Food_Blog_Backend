from abc import ABC, abstractmethod
from Repositories.interface_database_connection import IDataBaseClient


class IRepository(ABC):
    def __init__(self, client: IDataBaseClient):
        self.client = client

    @abstractmethod
    def save(self):
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
