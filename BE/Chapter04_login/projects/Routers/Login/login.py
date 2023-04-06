from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ...functions import functions
from ...setting import oauth2_scheme
from ...models import models

router = APIRouter(
    prefix="",
    tags=["Login/token"]
)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(functions.get_db)):
    # kiểm tra dữ liệu

    pass




# @router.post("/login")
# async def login_for_access_token(form_data: schemas.TokenData, db: Session = Depends(functions.get_db)):
#     pass
