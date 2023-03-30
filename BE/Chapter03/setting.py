from sqlalchemy import create_engine, or_
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database = dict(
    drivername='mssql',
    username='123123123123',
    password='1231231233am',
    host='1231231231239',
    database='1231231231',
    query={"driver": 'SQL Server Native Client 11.0'}
)

url = URL.create(**database)
engine = create_engine(url=url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

