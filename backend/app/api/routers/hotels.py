from fastapi import APIRouter

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

# Временные данные для проверки API
hotels = [
    {
        "id": 1,
        "name": "Полярная звезда",
        "address": "г. Красноярск",
        "description": "Уютный мини-отель"
    }
]


@router.get("/")
def get_hotels():
    """Получить список всех отелей."""
    return hotels


@router.get("/{hotel_id}")
def get_hotel(hotel_id: int):
    """Получить информацию об одном отеле."""
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            return hotel

    return {"message": "Отель не найден"}
