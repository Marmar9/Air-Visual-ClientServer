from typing import Union
from datarepository import DataRepository
from models import Data
from .utils import compute_hour_difference

class GetDataController:
    __repository: DataRepository
    def __init__(self, repository) -> None:
        self.__repository = repository

    def getData(self, timestamp : str) -> Union[Data, None]:
        data = self.__repository.getData()
        data_keys = list(data.keys())
        if len(data_keys) == 0:
            return

        first_one = data[data_keys[0]]
        bestMatch = {'timestamp': first_one.current.weather.ts, 'hour_difference': compute_hour_difference(first_one.current.weather.ts, timestamp)}

        for key in data.keys():
            new_timestamp = data[key].current.weather.ts
            hour_difference = compute_hour_difference(new_timestamp, timestamp)
            if  hour_difference < bestMatch["hour_difference"]:
                bestMatch = {'timestamp': first_one.current.weather.ts, 'hour_difference': compute_hour_difference(first_one.current.weather.ts, timestamp) }

        return data[bestMatch['timestamp']]
