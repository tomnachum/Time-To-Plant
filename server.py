from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
async def get_client():
    return FileResponse('client\index.html')


@app.get("/images/{image_name}")
async def images(image_name):
    return FileResponse(f"plants-img\\{image_name}")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
