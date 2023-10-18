from fastapi import FastAPI
from loguru import logger
from api.api import api_router


def init(app: FastAPI):
    logger.info("Init application")
    add_routers(app)


def add_routers(app: FastAPI):
    app.include_router(api_router)