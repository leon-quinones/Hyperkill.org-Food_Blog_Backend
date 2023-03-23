from Model.quantity.quantity_entity import Quantity
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.base_repository import BaseRepository


class QuantityRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient):
        super().__init__(database_connection, 'quantity', Quantity)