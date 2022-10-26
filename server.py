from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import db_manager


app = FastAPI()


app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
def get_client():
    return FileResponse("client\index.html")


@app.get("/profile")
def get_user_profile():
    return FileResponse("client\profile.html")


@app.get("/plants")
def get_plants():
    return db_manager.get_all_plants()


@app.get("/plants/{user_id}")
def get_user_plant(user_id):
    return db_manager.get_user_plants(user_id)


@app.get("/images/{image_name}")
def images(image_name):
    return FileResponse(f"plants-img\\{image_name}")


@app.post("/users/{user_id}/plants/{plant_id}")
def add_plant_to_user(user_id, plant_id):
    db_manager.add_notification(user_id, plant_id, "")
    db_manager.add_plants_to_user(user_id, [plant_id])


@app.delete("/users/{user_id}/plants/{plant_id}")
def delete_plant_of_user(user_id, plant_id):
    db_manager.delete_notification(user_id, plant_id)
    db_manager.delete_plant_of_user(user_id, plant_id)
    return db_manager.get_user_plants(user_id)


@app.put("/users/{user_id}/plants/{plant_id}")
async def update_note(user_id, plant_id, request: Request):
    body = await request.json()
    return db_manager.update_note(user_id, plant_id, body["noteStr"])


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
