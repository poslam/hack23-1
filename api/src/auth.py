from datetime import datetime, timedelta

from config import (ALGORITHM, AUTH_TOKEN_LIFE, REFRESH_TOKEN_LIFE, RT_SECRET,
                    SECRET_AUTH)
from database.models import RefreshTokenStorage, User
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from jwt import decode, encode
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils import name_maker, time
from werkzeug.security import check_password_hash, generate_password_hash

from database.database import get_session

auth_router = APIRouter(
    prefix="/auth"
)


async def type_required(types: list,  auth: str = Header(None),
                        session: AsyncSession = Depends(get_session)):
    data = None
    try:
        data = decode(auth, SECRET_AUTH, algorithms=[ALGORITHM])

        token_expired_time = datetime.strptime(
            data["expired"], "%Y-%m-%d %H:%M:%S.%f")

        if token_expired_time < time():
            raise Exception
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="token is invalid")

    user = await session.get(User, data["id"])

    if user == None:
        raise HTTPException(status_code=400, detail="user not found")

    if types != []:
        if user.type.name not in types:
            raise HTTPException(status_code=403, detail="not allowed")

    return user


async def login_required(auth: str = Header(None),
                         session: AsyncSession = Depends(get_session)):
    return await type_required([], auth, session)


async def admin_required(auth: str = Header(None),
                         session: AsyncSession = Depends(get_session)):
    return await type_required(["admin"], auth, session)


async def driver_required(auth: str = Header(None),
                          session: AsyncSession = Depends(get_session)):
    return await type_required(["driver"], auth, session)


async def packer_required(auth: str = Header(None),
                          session: AsyncSession = Depends(get_session)):
    return await type_required(["packer"], auth, session)


def make_token(user_id: int):
    return encode(
        {"id": user_id, "expired": str(
            time() + timedelta(hours=int(AUTH_TOKEN_LIFE)))},
        SECRET_AUTH,
    )


def make_refresh_token(user_id: int):
    return encode(
        {"id": user_id, "expired": str(
            time() + timedelta(days=int(REFRESH_TOKEN_LIFE)))},
        RT_SECRET
    )


@auth_router.post("/login")
async def login(request: Request,
                session: AsyncSession = Depends(get_session)):
    try:
        data = await request.json()

        email = data["email"]
        password = data["password"]
    except:
        raise HTTPException(status_code=400, detail="incorrect request")

    stmt = select(User.id,
                  User.email,
                  User.first_name,
                  User.second_name,
                  User.third_name,
                  User.type,
                  User.password).where(User.email == email)
    user = (await session.execute(stmt)).first()

    if user != None:
        user = dict(user._mapping)

    else:
        raise HTTPException(status_code=400, detail="user doesn't exist")

    if check_password_hash(user["password"], password):

        return {"token": make_token(user["id"]),
                "refresh_token": make_refresh_token(user["id"]),
                "type": user["type"],
                "name": name_maker(user)["name"]}

    raise HTTPException(status_code=400, detail="wrong auth data")


@auth_router.post("/signup")
async def signup(request: Request,
                 session: AsyncSession = Depends(get_session)):
    try:
        data = await request.json()
        first_name = data["first_name"]
        second_name = data["second_name"]
        third_name = data["third_name"]
        email = data["email"]
        type = data["type"]
        car_num = data["car_num"]
        expedition = data["expedition"]
        password = data["password"]
    except:
        raise HTTPException(status_code=400, detail="incorrect request")

    user_raw = (await session.execute(
        select(User).where(User.email == email)
    )).first()

    if user_raw != None:
        raise HTTPException(
            status_code=400, detail="email address already in use")

    if type not in ["admin", "driver", "packer"]:
        raise HTTPException(status_code=400, detail="wrong user type")

    user_insert = {
        "first_name": first_name,
        "second_name": second_name,
        "third_name": third_name,
        "email": email,
        "type": type,
        "car_num": car_num,
        "expedition": expedition,
        "password": generate_password_hash(password),
    }

    stmt = insert(User).values(user_insert)

    try:
        await session.execute(stmt)
        await session.commit()
        return {"detail": "successfully registered"}
    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="smth gone wrong")


@auth_router.post("/refresh")
async def refresh(request: Request,
                  session: AsyncSession = Depends(get_session)):
    try:
        data = await request.json()

        refresh_token_recieved = data["refresh_token"]

        token_data = decode(refresh_token_recieved, RT_SECRET,
                            algorithms=[ALGORITHM])

        token_expired_time = datetime.strptime(
            token_data["expired"], "%Y-%m-%d %H:%M:%S.%f")

        if token_expired_time < time():
            raise Exception

    except:
        raise HTTPException(status_code=400, detail="token is invalid")

    tokens = (await session.execute(
        select(RefreshTokenStorage.id,
               RefreshTokenStorage.refresh_token,
               RefreshTokenStorage.expired)
    )).all()

    for token in tokens:
        token = token._mapping

        if token["expired"] < time():
            await session.execute(
                delete(RefreshTokenStorage)
                .where(RefreshTokenStorage.id == token["id"])
            )
            await session.commit()

        if token["refresh_token"] == refresh_token_recieved:
            raise HTTPException(status_code=400, detail="token is invalid")

    user_id = token_data["id"]

    user = await session.get(User, user_id)

    if user == None:
        raise HTTPException(status_code=400, detail="user not found")

    user_type = (await session.get(User, user_id)).type.name

    await session.execute(
        insert(RefreshTokenStorage).values({
            "refresh_token": refresh_token_recieved,
            "expired": token_expired_time
        })
    )

    await session.commit()

    return {"token": make_token(user_id),
            "refresh_token": make_refresh_token(user_id),
            "type": user_type
            }
