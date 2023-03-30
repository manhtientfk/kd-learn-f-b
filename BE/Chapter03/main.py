from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


def HTTP_RETURN(data, status_code: int | None = 0, detail: str | None = ""):
    return {
        "status": status_code,
        "detail": detail,
        "data": data if data else None
    }


# @app.get("/path")
# async def main(a: int, b: int):
#     sums = a + b
#     return HTTP_RETURN(data=sums, status_code=200, detail="Tính tổng thành công")


"""
    account {
    us : str
    pw : str
    student_code : int
    }
"""


lstAccount = [{
    "us": "us1",
    "pw": "pw1",
    "student_code": 1
}, {
    "us": "us2",
    "pw": "pw2",
    "student_code": 2
}, {
    "us": "us3",
    "pw": "pw3",
    "student_code": 3
}
]
lstStudent = []


class Account(BaseModel):
    us: str
    pw: str
    student_code: int


@app.post("/create-account")
async def createAccount(formdata: Account):
    # duyệt qua danh sách account cũ ==> dùng for
    # kiểm tra us có tồn tại hay chưa ==> dùng if
    # nếu chưa có thì thêm vào mảng lstAccount
    # nếu chưa có thì xuất data = None và detail = "tài khoản đã tồn tại"
    # chạy for i in lstAccount
    # nếu i.us == formdata.us
    # thì xuất ra là tài khoản đã tồn tại
    # còn lại thì thêm vào lstAccount
    for i in lstAccount:
        if i.get("us") == formdata.us:
            return HTTP_RETURN(data=None, status_code=204, detail="Tài khoản đã tồn tại")
    lstAccount.append(formdata.dict())
    return HTTP_RETURN(data=formdata, status_code=201, detail="Tạo mới thành công")


@app.get("/show-account")
async def showAccount():
    return HTTP_RETURN(data=lstAccount, status_code=200, detail="Lấy dữ liệu thành công")

# Cách 2

# Tìm kiếm theo student_code


@app.get("/detail-account/{student_code}")
async def detailAccount(student_code: int):
    data_account = None
    for i in lstAccount:
        if i["student_code"] == student_code:
            data_account = i
    return HTTP_RETURN(data=data_account, status_code=200, detail="Lấy chi tiết account thành công")
# Cách 1
# @app.get("/detail-account")
# async def detailAccount(student_code: int):
#     data_account = None
#     for i in lstAccount:
#         if i["student_code"] == student_code:
#             data_account = i
#     return HTTP_RETURN(data=data_account, status_code=200, detail="Lấy chi tiết account thành công")

# Tìm theo us


@app.get("/detail-account-by-us/{us}")
async def detailAccount(us: str):
    data_account = None
    for i in lstAccount:
        if i["us"] == us:
            data_account = i
    return HTTP_RETURN(data=data_account, status_code=200, detail="Lấy chi tiết account thành công")
