from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi import FastAPI
from pathlib import Path
import os
from fastapi import FastAPI

DEBUG = False
MIDDLEWARE = []
ALGORITHM = "HS256"
ALLOWED_HOSTS = ["*"]
ACCESS_TOKEN_EXPIRE_MINUTES = 30
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "09d25e094faa6ca2123qwe12313312312f312e1237099f6f312f4caa316cf63231b88e8d3e7"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# app = FastAPI(docs_url=False, redoc_url=False)
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = dict(
    drivername='mssql',
    username='Tên đăng nhập',
    password='mật khẩu',
    host='host là tên server',
    database='tên database',
    query={"driver": 'SQL Server Native Client 11.0'}
)

# database = dict(
#     drivername='mssql',
#     username='sa1',
#     password='123',
#     host='IT03\TIEN',
#     database='TBSL_ERP',
#     query={"driver": 'SQL Server Native Client 11.0'}
# )


url = URL.create(**database)
engine = create_engine(url=url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


STATIC = "/static/"
STATIC_FILE = os.path.join(BASE_DIR, "static_file")
STATIC_FILES = "static_file"
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
