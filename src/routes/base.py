from fastapi import FastAPI , APIRouter
base_router = APIRouter(

prefix = "/api/v1", ## to make it easy to change in future all api 
tags = ["api_v1"],

)

@base_router.get("/")

async def welcom(): ## async help in future to improve performance 

    return{
    "message" : "444hello all!" 
}



