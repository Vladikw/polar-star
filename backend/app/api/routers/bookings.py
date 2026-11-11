
from datetime import date
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)
