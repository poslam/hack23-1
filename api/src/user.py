from fastapi import APIRouter, Depends
from src.auth import login_required

user_router = APIRouter(
    prefix="/user"
)


@user_router.get('/view')
async def user_view(user=Depends(login_required)):
    return user
