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
            "number": 1,
            "status": 1,
            "time": 30,
            "gateNumber": None,
            "productList": [
                {
                    "productName": "Сушки 'Кроха'",
                    "productSize": "18 X 10 шт"
                },
                {
                    "productName": "Пряники 'Шоколадные' крупные",
                    "productSize": "12 X 25 шт"
                },
                {
                    "productName": "Пряники Заварные с начинкой 'абрикос'",
                    "productSize": "12 X 20 шт"
                },
                {
                    "productName": "Вафли со вкусом 'Лимонад' (квадратини)",
                    "productSize": "36 X 10 шт"
                },
                {
                    "productName": "Сухари 'Киевские'",
                    "productSize": "30 X 90 шт"
                },
                {
                    "productName": "Сухари 'Сливочные'",
                    "productSize": "30 X 150 шт"
                },
                {
                    "productName": "Сухари 'С маком'",
                    "productSize": "30 X 20 шт"
                }
            ]
        },
        {
            "number": 2,
            "status": 2,
            "time": 15,
            "gateNumber": None,
            "productList": [
                {
                    "productName": "Сушки 'Саша'",
                    "productSize": "18 X 4 шт"
                },
                {
                    "productName": "Пряники 'Сливочные' крупные",
                    "productSize": "10 X 3 шт"
                }
            ]
        },
        {
            "number": 3,
            "status": 3,
            "time": None,
            "gateNumber": 5,
            "productList": [
                {
                    "productName": "Сухари 'Сыр'",
                    "productSize": "30 X 124 шт"
                },
                {
                    "productName": "Вафли 'Шоколад'",
                    "productSize": "60 X 5 шт"
                },
                {
                    "productName": "Пряники Заварные с начинкой 'молоко'",
                    "productSize": "12 X 15 шт"
                }
            ]
        },
        {
            "number": 4,
            "status": 1,
            "time": 7,
            "gateNumber": None,
            "productList": [
                {
                    "productName": "Сухари 'Колбаса'",
                    "productSize": "30 X 131 шт"
                },
                {
                    "productName": "Пряники 'Шоколад'",
                    "productSize": "10 X 15 шт"
                },
                {
                    "productName": "Пряники Заварные с начинкой 'молоко'",
                    "productSize": "12 X 17 шт"
                }
            ]
        }
    ]


@driver_router.get("/unload_points_view")
async def unload_points_view(user=Depends(driver_required)):
    return [
        {
            "tripNumber": 1,
            "tripPointList": [
                {
                    "pointName": "Фадеевский",
                    "address": "ул. Фадеева, 45Б",
                    "orderNumber": 123444
                },
                {
                    "pointName": "Реми",
                    "address": "ул. Адмирала Юмашева, 14Г",
                    "orderNumber": 999812,
                },
                {
                    "pointName": "Виктория",
                    "address": "ул. Борисенко 68, стр 1",
                    "orderNumber": 123881,
                },
                {
                    "pointName": "Нейбута",
                    "address": "ул. Нейбута, 8Г",
                    "orderNumber": 567812,
                },
                {
                    "pointName": "Трио",
                    "address": "ул. Каплунова, 3",
                    "orderNumber": 998712,
                },
                {
                    "pointName": "Дуэт",
                    "address": "ул. Каплунова, 2",
                    "orderNumber": 789123,
                },
                {
                    "pointName": "Есо маркет",
                    "address": "ул. Луговая, 89А",
                    "orderNumber": 398123,
                }
            ]
        }
    ]
