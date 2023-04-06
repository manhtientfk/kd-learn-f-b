from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ...functions import functions as deps
from ...setting import oauth2_scheme
from ...models import models
from ...schemas import schemas
router = APIRouter(
    prefix="",
    tags=["account"]
)

@router.post("/insert")
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    account: schemas.Account,
):
    account = models.Account(**account.dict())
    db.add(account)
    db.commit()
    return deps.HTTP_RETURN(status_code=200,detail="Thêm tài khoản thành công")



# @router.post("/login")
# async def login_for_access_token(form_data: schemas.TokenData, db: Session = Depends(functions.get_db)):
#     pass
