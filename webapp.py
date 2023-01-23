import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

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

languages = ["en", "de"]
default_fallback = "en"

@app.get("/")
def landing(request: Request) -> Response:
    return RedirectResponse(request.url_for("landing_locale", locale="en"))

@app.get("/{locale}")
def landing_locale(request: Request, locale: str) -> Response:
    compile_scss_files()
    if locale not in languages:
        locale = default_fallback
    return templates.TemplateResponse(f"index_{locale}.html", {"request": request, "locale": locale})


@app.get("/{locale}/imprint")
def imprint(request: Request, locale: str) -> Response:
    compile_scss_files()
    if locale not in languages:
        locale = default_fallback
    return templates.TemplateResponse(f"imprint_{locale}.html", {"request": request, "locale": locale})


@app.get("/{locale}/privacy")
def privacy(request: Request, locale: str) -> Response:
    compile_scss_files()
    if locale not in languages:
        locale = default_fallback
    return templates.TemplateResponse(f"privacy_{locale}.html", {"request": request, "locale": locale})


@app.get("/{locale}/publications")
def publications(request: Request, locale: str) -> Response:
    compile_scss_files()
    if locale not in languages:
        locale = default_fallback
    return templates.TemplateResponse(f"publications_{locale}.html", {"request": request, "locale": locale})
