import datetime
from typing_extensions import Annotated

from fastapi import APIRouter, Request, Form
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
    search: Annotated[str, Form()] = None,
):  
    context = {"request": request}

    print("Searching:", search)
    # dummy
    if search:
        results = [f"{search} - result {i}" for i in range(5)]
        context["results"] = results

    return templates.TemplateResponse(
            name="recommender.html", 
            context=context,
        )
