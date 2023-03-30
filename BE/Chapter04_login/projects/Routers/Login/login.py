from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends,  status, APIRouter
from sqlalchemy.orm import Session
from ...models import models
from ...functions import functions
from ...schemas import schemas
from ...setting import oauth2_scheme

router = APIRouter(
    prefix="",
    tags=["Login/token"]
)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(functions.get_db)):
    pass


@router.post("/login")
async def login_for_access_token(form_data: schemas.TokenData, db: Session = Depends(functions.get_db)):
    pass
