from fastapi import APIRouter, Depends

from src.auth import packer_required

packer_router = APIRouter(
    prefix="/packer"
)


@packer_router.post("/take_order")
async def take_order(user=Depends(packer_required)):
    return {"detail": "take order success"}


@packer_router.post("/untake_order")
async def take_order(user=Depends(packer_required)):
    return {"detail": "untake order success"}


@packer_router.post("/end_order")
async def end_order(user=Depends(packer_required)):
    return {"detail": "end order success"}


@packer_router.get("/order_view")
async def order_view(user=Depends(packer_required)):
    return [
        {
            "tripNumber": 1,
            "status": 1,
            "time": 30,
            "driver": {
                "id": 1,
                "name": "Василий Иванович",
                "car_num": "о123оо25",
            },
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
            "tripNumber": 2,
            "status": 2,
            "time": 15,
            "driver": {
                "id": 1,
                "name": "Василий Иванович",
                "car_num": "о123оо25",
            },
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
            "tripNumber": 3,
            "status": 3,
            "time": None,
            "driver": {
                "id": 1,
                "name": "Василий Иванович",
                "car_num": "о123оо25",
            },
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
            "tripNumber": 4,
            "status": 1,
            "time": 7,
            "driver": {
                "id": 1,
                "name": "Василий Иванович",
                "car_num": "о123оо25",
            },
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