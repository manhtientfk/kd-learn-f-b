import datetime
from sqlalchemy import or_, and_, Table, DateTime, Boolean, ForeignKey, Column, NVARCHAR, Integer, VARCHAR, String, Float, or_, and_
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import Session
from projects.setting import Base, engine, SessionLocal

db = SessionLocal()


class Account(Base):
    __tablename__ = "account"
    us = Column(VARCHAR(length=64),primary_key = True)
    pw = Column(VARCHAR(length=400))
    isdelete = Column(Boolean(),default = False)


class Candicate(Base):
    __tablename__ = "candicate"
    candicateCode = Column(VARCHAR(length=20),primary_key = True)
    name = Column(NVARCHAR(length=64))
    age = Column(Integer())
    us = Column(VARCHAR(length=64),ForeignKey("account.us"))
    isdelete = Column(Boolean(),default = False)



class Choice(Base):
    __tablename__ = "choice"
    id = Column(Integer(),primary_key = True)
    title = Column(NVARCHAR(length=20))
    anwser = Column(NVARCHAR(length=500))
    isdelete = Column(Boolean(),default = False)


class Question(Base):
    __tablename__ = "question"
    questionCode = Column(Integer(),primary_key = True)
    title = Column(NVARCHAR(length=20))
    question = Column(NVARCHAR(length=500))
    result = Column(NVARCHAR(length=500))
    choise = Column(Integer(),ForeignKey("choice.id"))
    point = Column(Float())
    isdelete = Column(Boolean(),default = False)



class Exam_Question(Base):
    __tablename__ = "Exam_Question"
    id = Column(Integer(),primary_key = True)
    questionCode = Column(Integer(),ForeignKey("question.questionCode"))
    maDeThi = Column(Integer(),ForeignKey("deThi.maDeThi"))
    isdelete = Column(Boolean(),default = False)


class DeThi(Base):
    __tablename__ = "deThi"
    maDeThi = Column(Integer(),primary_key = True)
    
    tenDeThi = Column(NVARCHAR(length=20))
    note = Column(NVARCHAR(length=500))
    isdelete = Column(Boolean(),default = False)



class Subject(Base):
    __tablename__ = "subject"
    subject_code = Column(Integer(),primary_key = True)
    subjectName = Column(NVARCHAR(length=500))
    isdelete = Column(Boolean(),default = False)

class Exam(Base):
    __tablename__ = "exam"
    examCode = Column(Integer(),primary_key = True)
    candicateCode = Column(VARCHAR(length=20),ForeignKey("candicate.candicateCode"))
    subject_code = Column(Integer(),ForeignKey("subject.subject_code"))
    maDeThi = Column(Integer(),ForeignKey("deThi.maDeThi"))
    Candicate_anwser = Column(Integer(),primary_key = True)



class Lst_Candicate_anwser(Base):
    __tablename__ = "Lst_Candicate_anwser"
    CandicateAnwserCode = Column(Integer(),primary_key = True) 
    anwser = Column(NVARCHAR(length=500))


Base.metadata.create_all(bind=engine)
