from abc import ABC, abstractmethod


class IDataBaseClient(ABC):
    @abstractmethod
    def connect(self, connection_string: str):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError