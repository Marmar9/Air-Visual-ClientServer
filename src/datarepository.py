from models import Data 
class DataRepository:
    __data_dict: dict[str, Data]

    def __init__(self) -> None:
        self.__data_dict = {}

    def addData(self, data: Data):
        self.__data_dict[data.current.weather.ts] = data

    def getData(self) -> dict[str, Data]:
        return self.__data_dict
