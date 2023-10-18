import datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = APIRouter()
templates = Jinja2Templates(directory="/Users/ryan/playground/python/projects/testing-web/views")

@app.get(
    "/",
    response_class=HTMLResponse,
)
async def get_recommender(
    request: Request,
):
    return templates.TemplateResponse(
            name="recommender.html", 
            context={
                "request": request,
                "id_": 123
                },
        )
    # value = f"Message generated at {datetime.datetime.now()}"
    # return {
    #     "data": {
    #         "message": value
    #     }
    # }
