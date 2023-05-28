from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/my", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("my.html", {"request": request, "title": "BreadCloud"})
