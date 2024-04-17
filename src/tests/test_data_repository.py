import pytest

from ..datarepository import DataRepository
from ..models import Location, Pollution, Weather, Current, Data

@pytest.fixture
def repository_instance():
    repository = DataRepository()

    location_data = {"type": "Point", "coordinates": [40.7128, -74.0060]}
    pollution_data = {"ts": "2024-04-17T12:00:00Z", "aqius": 55, "mainus": "pm25", "aqicn": 70, "maincn": "pm10"}
    weather_data = {"ts": "2024-04-17T12:00:00Z", "tp": 20, "pr": 1015, "hu": 60, "ws": 5.5, "wd": 180, "ic": "clear"}
    
    location = Location(**location_data)
    pollution = Pollution(**pollution_data)
    weather = Weather(**weather_data)
    current = Current(pollution=pollution, weather=weather)
    
    data = Data(
        city="New York",
        state="NY",
        country="USA",
        location=location,
        current=current
    )
    repository.addData(data)
    return repository

def test_get_data(repository_instance: DataRepository):
    data = repository_instance.getData()
    assert len(data) == 1

def test_add_data(repository_instance: DataRepository):
    location_data = {"type": "Point", "coordinates": [40.7128, -74.0060]}
    pollution_data = {"ts": "2024-04-22:00:00Z", "aqius": 55, "mainus": "pm25", "aqicn": 70, "maincn": "pm10"}
    weather_data = {"ts": "2024-04-22:00:00Z", "tp": 20, "pr": 1015, "hu": 60, "ws": 5.5, "wd": 180, "ic": "clear"}
    
    location = Location(**location_data)
    pollution = Pollution(**pollution_data)
    weather = Weather(**weather_data)
    current = Current(pollution=pollution, weather=weather)
    
    data = Data(
        city="New York",
        state="NY",
        country="USA",
        location=location,
        current=current
    )
    repository_instance.addData(data)
    data = repository_instance.getData()

    assert len(data) == 2
