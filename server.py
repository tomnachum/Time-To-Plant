from fastapi import FastAPI, Request, Response
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests

from db_manager import get_all_plants

app = FastAPI()

# JS_FILES_DIR = "client/build"
# TEMPLATE_DIR = "client/src"
# HTML_DIR = "client\src\index.html"

# app.mount(
#     f"/{JS_FILES_DIR}",
#     StaticFiles(directory=JS_FILES_DIR),
#     name=JS_FILES_DIR,
# )

# app.mount(
#     f"/{TEMPLATE_DIR}",
#     StaticFiles(directory=TEMPLATE_DIR),
#     name=TEMPLATE_DIR,
# )


# @app.get("/")
# def get_html():
#     return FileResponse(HTML_DIR)


@app.get("/plants")
def get_plants():
    return get_all_plants()


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
