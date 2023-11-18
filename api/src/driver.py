from database.models import User
from fastapi import APIRouter, Depends
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth import driver_required

from database.database import get_session

driver_router = APIRouter(
    prefix="/driver"
)


@driver_router.post("/start_shift")
async def start_shift(user=Depends(driver_required),
                      session: AsyncSession = Depends(get_session)):

    await session.execute(
        update(User).where(User.id == user.id).values(active_shift=True)
    )
    await session.commit()

    return {"detail": "start shift success"}


@driver_router.post("/end_shift")
async def end_shift(user=Depends(driver_required),
                    session: AsyncSession = Depends(get_session)):

    await session.execute(
        update(User).where(User.id == user.id).values(active_shift=False)
    )
    await session.commit()

    return {"detail": "end shift success"}


@driver_router.post("/take_order")
async def take_order(user=Depends(driver_required)):
    return {"detail": "take order success"}


@driver_router.post("/untake_order")
async def take_order(user=Depends(driver_required)):
    return {"detail": "untake order success"}


@driver_router.get("/collect_view")
async def collect_view(user=Depends(driver_required)):
    return [
        {
            "departament": "Экспедиция 1",
            "status": "started",
            "end_time": "hours=0,minutes=30",
            "gate": None,
            "products": [
                {
                    "name": "Сушки 'Кроха'",
                    "pack": 18,
                    "size": 10
                },
                {
                    "name": "Пряники 'Шоколадные' крупные",
                    "pack": 12,
                    "size": 15
                },
                {
                    "name": "Пряники Заварные с начинкой 'абрикос'",
                    "pack": 12,
                    "size": 15
                },
                {
                    "name": "Вафли со вкусом 'Лимонад' (квадратини)",
                    "pack": 36,
                    "size": 10
                },
                {
                    "name": "Сухари 'Киевские'",
                    "pack": 30,
                    "size": 20
                },
                {
                    "name": "Сухари 'Сливочные'",
                    "pack": 30,
                    "size": 5
                },
                {
                    "name": "Сухари 'С маком'",
                    "pack": 30,
                    "size": 100
                }
            ]
        },
        {
            "departament": "Экспедиция 2",
            "status": "in progress",
            "end_time": "hours=0,minutes=15",
            "gate": None,
            "products": [
                {
                    "name": "Сушки 'Саша'",
                    "pack": 18,
                    "size": 120
                },
                {
                    "name": "Пряники 'Сливочные' крупные",
                    "pack": 10,
                    "size": 100
                }
            ]
        },
        {
            "departament": "Экспедиция 3",
            "status": "done",
            "end_time": None,
            "gate": "A5",
            "products": [
                {
                    "name": "Сухари 'Сыр'",
                    "pack": 30,
                    "size": 150
                },
                {
                    "name": "Вафли 'Шоколад'",
                    "pack": 60,
                    "size": 18
                },
                {
                    "name": "Пряники Заварные с начинкой 'молоко'",
                    "pack": 12,
                    "size": 15
                }
            ]
        }
    ]
