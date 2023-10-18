from fastapi import APIRouter

from api import recommender


api_router = APIRouter()
api_router.include_router(
    recommender.app,
    prefix="/recommender",
    tags=["recommender"],
)