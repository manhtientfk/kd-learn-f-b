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
def insertAccount(
    *,
    db: Session = Depends(deps.get_db),
    account: schemas.Account,
):
    account = models.Account(**account.dict())
    db.add(account)
    db.commit()
    return deps.HTTP_RETURN(status_code=200,detail="Thêm tài khoản thành công")



@router.put("/update-pw")
def updateAccount(
    *,
    db: Session = Depends(deps.get_db),
    account: schemas.Account,
):
    # kiểm tra tài khoản đã tồn tại hay chưa bằng phương thức filter.   .first() lây 1 giá trị duy nhất đầu tiên, .all() lấy hết tất cả giá trị
    checkAC = db.query(models.Account).filter(models.Account.us == account.us).filter(models.Account.isdelete == False).first()
    # tương ứng với sql select top 1 * from account where us = account.us  and isdelete = 0
    # kiểm gia biến checkAC có giá trị hay chưa
    if checkAC:
        # nếu có giá trị thì cập nhật
        checkAC.pw = account.pw
        # lưu lại giá trị đã thay đổi vào database
        db.commit()
        # trả về giá trị và thông báo cho font end biết là backend đã cập nhật thành công
        return deps.HTTP_RETURN(status_code=200,detail="Cập nhật lại mật khẩu mới thành công")
    # trường hợp còn lại là tài khoản không tồn tại
    return deps.HTTP_RETURN(status_code=204,detail="Tài khoản us nhập vào không tồn tại")



@router.delete("/delete-ac/{us}")
def deleteAccount(us: str , db: Session = Depends(deps.get_db),
):
    # kiểm tra tài khoản đã tồn tại hay chưa bằng phương thức filter.   .first() lây 1 giá trị duy nhất đầu tiên, .all() lấy hết tất cả giá trị
    checkAC = db.query(models.Account).filter(models.Account.us == us).filter(models.Account.isdelete == False).first()
    # tương ứng với sql select top 1 * from account where us = account.us  and isdelete = 0
    # kiểm gia biến checkAC có giá trị hay chưa
    if checkAC:
        # nếu có giá trị thì cập nhật
        checkAC.isdelete = True
        # lưu lại giá trị đã thay đổi vào database
        db.commit()
        # trả về giá trị và thông báo cho font end biết là backend đã cập nhật thành công
        return deps.HTTP_RETURN(status_code=200,detail="Đã xóa tài khoản có us: " + us + " thành công")
    # trường hợp còn lại là tài khoản không tồn tại
    return deps.HTTP_RETURN(status_code=204,detail="Tài khoản us cần xóa không tồn tại")

# lấy chi tiết tài khoản có us = us
@router.get("/detail-ac/{us}")
def detailccount(us: str , db: Session = Depends(deps.get_db)):
    # kiểm tra tài khoản đã tồn tại hay chưa bằng phương thức filter.   .first() lây 1 giá trị duy nhất đầu tiên, .all() lấy hết tất cả giá trị
    checkAC = db.query(models.Account).filter(models.Account.us == us).filter(models.Account.isdelete == False).first()
    # tương ứng với sql select * from account where us = account.us  and isdelete = 0
    # kiểm gia biến checkAC có giá trị hay chưa
    if checkAC:
        # nếu có giá trị thì trả về giá trị đã lấy
        return deps.HTTP_RETURN(status_code=200,detail="Lấy thông tin thành công",data=checkAC)
    # trường hợp còn lại là tài khoản không tồn tại
    return deps.HTTP_RETURN(status_code=204,detail="Tài khoản us không tồn tại")

# lấy danh sách các tài khoản 
@router.get("/detail-ac")
def listaccAccount(db: Session = Depends(deps.get_db),
):
    # kiểm tra tài khoản đã tồn tại hay chưa bằng phương thức filter.   .first() lây 1 giá trị duy nhất đầu tiên, .all() lấy hết tất cả giá trị
    checkAC = db.query(models.Account).filter(models.Account.isdelete == False).all()
    # tương ứng với sql select * from account where  isdelete = 0
    # kiểm gia biến checkAC có giá trị hay chưa
    if checkAC:
        # nếu có giá trị thì trả về giá trị đã lấy
        return deps.HTTP_RETURN(status_code=200,detail="Lấy thông tin thành công",data=checkAC)
    # trường hợp còn lại là tài khoản không tồn tại
    return deps.HTTP_RETURN(status_code=204,detail="Tài khoản us không tồn tại")





