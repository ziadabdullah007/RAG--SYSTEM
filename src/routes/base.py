from fastapi import FastAPI , APIRouter
from helpers.config import get_settings
base_router = APIRouter(

prefix = "/api/v1", ## to make it easy to change in future all api 
tags = ["api_v1"],

)

@base_router.get("/")
async def welcom(): ## async help in future to improve performance 
    app_settings = get_settings() ## to read the config file and use it in the code
    app_name = app_settings.app_name ## to get the app name from the config file
    return{
    "message" : "444hello all!",
    "app_name" : app_name,
}



