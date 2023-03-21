from Model.measure.meaure_entity import Measure
from Repositories.interfaces.interface_database_connection import IDataBaseClient
from Repositories.base_repository import BaseRepository


class MeasureRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient, model_name: str):
        self.super().__init__(database_connection, model_name, Measure)