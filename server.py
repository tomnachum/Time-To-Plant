from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from db_manager import get_all_plants

app = FastAPI()

app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
def get_client():
    return FileResponse('client\index.html')


@app.get("/plants")
def get_plants():
    return get_all_plants()


@app.get("/images/{image_name}")
def images(image_name):
    return FileResponse(f"plants-img\\{image_name}")


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
