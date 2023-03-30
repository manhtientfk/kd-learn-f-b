import datetime
from sqlalchemy import inspect
from jose import jwt
from ..setting import SessionLocal
from datetime import timedelta
from ..setting import *
from typing import Optional, Union

# hàm trả về


def HTTP_RETURN(status_code, detail, header: dict | None = {}, data: Union[list, dict] | None = {}):
    return {
        'status_code': status_code,
        'detail': detail,
        'header': header,
        'data': data
    }

# hàm kết nối csdl


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# hàm chuyển đổi object to dic


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

# hàm kiểm tra mật khẩu


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# hàm băm password


def get_password_hash(password):
    return pwd_context.hash(password)

# hàm tạo token từ data


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(days=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# hàm lấy data từ token


def getDataToken(token: str):
    return jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)
