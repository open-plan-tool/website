import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.compile_scss import convert_scss_to_css

app = FastAPI()

SERVER_ROOT = os.path.dirname(__file__)
STATIC_FOLDER = "static"


def compile_scss_files():
    """compile scss files in /static/css folder to css files"""
    convert_scss_to_css(
        [
            os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
            for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
            if f.endswith("scss")
        ]
    )


app.mount(
    "/" + STATIC_FOLDER,
    StaticFiles(directory=os.path.join(SERVER_ROOT, STATIC_FOLDER)),
    name=STATIC_FOLDER,
)

templates = Jinja2Templates(directory=os.path.join(SERVER_ROOT, "templates"))


@app.get("/")
def landing(request: Request) -> Response:
    compile_scss_files()
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/imprint")
def imprint(request: Request) -> Response:
    compile_scss_files()
    return templates.TemplateResponse("imprint.html", {"request": request})


@app.get("/privacy")
def privacy(request: Request) -> Response:
    compile_scss_files()
    return templates.TemplateResponse("privacy.html", {"request": request})


@app.get("/publications")
def publications(request: Request) -> Response:
    compile_scss_files()
    return templates.TemplateResponse("publications.html", {"request": request})
