from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from app.bookings.router import get_bookings
from app.hotels.rooms.router import get_rooms_by_hotel
from app.hotels.router import get_hotels_by_location

router = APIRouter(
    prefix="/pages",
    tags=["Фронт"],
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(name="register.html", context={"request": request})


@router.get("/auth", response_class=HTMLResponse)
async def auth(request: Request):
    return templates.TemplateResponse(name="auth.html", context={"request": request})


@router.get("/find_hotels", response_class=HTMLResponse)
async def find_hotels(request: Request):
    return templates.TemplateResponse(name="find_hotels.html", context={"request": request})


@router.get("/hotels")
async def get_hotels_page(
        request: Request,
        hotels=Depends(get_hotels_by_location),
):
    return templates.TemplateResponse(name="hotels.html", context={"request": request, "hotels": hotels})


@router.get("/hotel_rooms", response_class=HTMLResponse)
async def hotel_rooms(request: Request,
                      rooms=Depends(get_rooms_by_hotel)
                      ):
    return templates.TemplateResponse(name="hotel_rooms.html", context={"request": request, "rooms": rooms})


@router.get("/my_bookings", response_class=HTMLResponse)
async def my_bookings(request: Request ):
    return templates.TemplateResponse(name="my_bookings.html", context={"request": request})
