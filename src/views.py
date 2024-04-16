from fastapi import APIRouter
from controllers.PostDataController import PostDataController
from models import PostDataModel, GetDataModel 
from datarepository import DataRepository
from controllers.GetDataController import GetDataController
import re

class AirVisualRouter(APIRouter):
    __GetDataController: GetDataController
    __PostDataController: PostDataController

    def __init__(self, GetDataController: GetDataController, PostDataController: PostDataController, **kwargs):
        super().__init__( **kwargs)
        self.__GetDataController = GetDataController
        self.__PostDataController = PostDataController

        @self.get("/data")
        async def get_data_handler(date:str):

            if not re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z', date):
                return 'Timestamp does not match the format "YYYY-MM-DDTHH:MM:SS.sssZ"'

            return self.__GetDataController.getData(date)
            
        @self.post("/data")
        async def post_data_handler(body: PostDataModel):
            self.__PostDataController.addData(body.data)
