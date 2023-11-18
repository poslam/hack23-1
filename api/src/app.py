from fastapi import FastAPI

from src.auth import auth_router
from src.driver import driver_router
from src.packer import packer_router
from src.user import user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(driver_router)
app.include_router(packer_router)
app.include_router(user_router)