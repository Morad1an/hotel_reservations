from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from app.admin.auth import authentication_backend
# from app.admin.views import UsersAdmin, BookingsAdmin, HotelsAdmin, RoomsAdmin
from app.config import settings
from app.database import engine
from app.hotels.router import router as router_hotels
from app.users.router import router as router_users
from app.images.router import router as router_images
from app.bookings.router import router as router_bookings
from app.pages.router import router as router_pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)
app.include_router(router_images)
app.include_router(router_pages)