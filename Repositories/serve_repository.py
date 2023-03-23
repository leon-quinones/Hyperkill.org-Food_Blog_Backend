from Model.serve.serve_entity import Serve
from Repositories.base_repository import BaseRepository
from Repositories.interfaces.interface_database_connection import IDataBaseClient


class ServeRepository(BaseRepository):

    def __init__(self, database_connection: IDataBaseClient):
        super().__init__(database_connection, 'serve', Serve)