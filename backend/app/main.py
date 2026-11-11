
from fastapi import FastAPI
from app.api.routers import hotels, rooms, bookings

app = FastAPI(
    title="Полярная звезда",
    description="Система управления сетью мини-отелей",
    version="0.1.0"
)


@app.get("/")
def home():
    return {"message": "Добро пожаловать в систему Полярная звезда!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(hotels.router)
app.include_router(rooms.router)
app.include_router(bookings.router)