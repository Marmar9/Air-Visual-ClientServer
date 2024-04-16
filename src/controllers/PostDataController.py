from datarepository import DataRepository
from models import Data


class PostDataController:
    __repository: DataRepository

    def __init__(self, repository: DataRepository) -> None:
        self.__repository = repository

    def addData(self, data: Data):
        self.__repository.addData(data)

        
