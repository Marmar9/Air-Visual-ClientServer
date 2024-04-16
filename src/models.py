from __future__ import annotations

from typing import List

from pydantic import BaseModel, constr

class Location(BaseModel):
    type: str
    coordinates: List[float]


class Pollution(BaseModel):
    ts: str
    aqius: int
    mainus: str
    aqicn: int
    maincn: str


class Weather(BaseModel):
    ts: str
    tp: int
    pr: int
    hu: int
    ws: float
    wd: int
    ic: str


class Current(BaseModel):
    pollution: Pollution
    weather: Weather


class Data(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: Current


class PostDataModel(BaseModel):
    status: str
    data: Data

class GetDataModel(BaseModel):
    status: str
    data: Data

