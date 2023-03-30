from sqlalchemy import Column, Boolean, Integer, String, NVARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, constr
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *


from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


data = []


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# thêm 1 book mới vào danh sách
# @app.post("/book")
# def add_book(book: Book):
#     data.append(book.dict())
#     return data

# # lấy danh sách hiện tại


# @app.get("/list")
# def get_books():
#     return data

# # lấy chi tiết sách có vị trí id


# @app.get("/book/{id}")
# def get_book(id: int):
#     id = id - 1
#     return data[id]

# # xóa book có vi trí id


# @app.delete("/book/{id}")
# def delete_book(id: int):
#     data.pop(id-1)
#     return data


class Account(Base):
    __tablename__ = 'account'
    us = Column(NVARCHAR(length=64), primary_key=True, nullable=False)
    pw = Column(NVARCHAR, unique=True)
    active = Column(Boolean)
    isdelete = Column(Boolean)


Base.metadata.create_all(bind=engine)


class s_Account(BaseModel):
    us: str
    pw: str
    active: bool
    isdelete: bool

    class Config:
        orm_mode = True


@app.post('/add_new', response_model=s_Account)
def add_book(account: s_Account, db: Session = Depends(get_db)):
    bk = Account(**account.dict())
    db.add(bk)
    db.commit()
    db.refresh(bk)
    return Account(**account.dict())


@app.get('/list', response_model=List[s_Account])
def get_books(db: Session = Depends(get_db)):
    recs = db.query(Account).all()
    return recs


@app.get('/book/{us}', response_model=s_Account)
def get_book(us: str, db: Session = Depends(get_db)):
    return db.query(Account).filter(Account.us == us).first()


@app.put('/update/{us}', response_model=s_Account)
def update_book(us: str, account: s_Account, db: Session = Depends(get_db)):
    ac = db.query(Account).filter(Account.us == us).first()
    ac.us = account.us
    ac.pw = account.pw
    ac.isdelete = account.isdelete
    ac.active = account.active
    db.commit()
    return db.query(Account).filter(Account.us == us).first()


@app.delete('/delete/{us}')
def del_book(us: int, db: Session = Depends(get_db)):
    try:
        db.query(Account).filter(Account.us == us).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"delete status": "success"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
