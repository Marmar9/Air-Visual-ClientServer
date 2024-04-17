from fastapi import FastAPI
from controllers.GetDataController import GetDataController
from controllers.PostDataController import PostDataController
from datarepository import DataRepository
from views import AirVisualRouter

app = FastAPI()

# Create an instance of CustomRouter
repository = DataRepository()
getDataController = GetDataController(repository)  
postDataController = PostDataController(repository)

router = AirVisualRouter(getDataController, postDataController)

# Mount the router on the main FastAPI application
app.include_router(router)

