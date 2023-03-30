import datetime
from sqlalchemy import or_, and_, Table, DateTime, Boolean, ForeignKey, Column, NVARCHAR, Integer, VARCHAR, String, Float, or_, and_
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import Session
from projects.setting import Base, engine, SessionLocal

db = SessionLocal()


Base.metadata.create_all(bind=engine)
