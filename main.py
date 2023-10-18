from fastapi import FastAPI
from loguru import logger
from core.init import init
from core.configs import setting


# init app
app = FastAPI()
init(app)
print(setting.REDIS.HOST)

@app.get("/")
async def howly():
    return {"status": "ok"}