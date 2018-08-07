#/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Integer, VARCHAR, ForeignKey,Text,String
from sqlalchemy import or_,and_

from DB.settings import *

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_email'
    id = Column(Integer,index=True,primary_key=True)
    email = Column(VARCHAR(20))
    password = Column(VARCHAR(20))
    last_login = Column(VARCHAR(30))
    jiachangcai = Column(Text)
    xiafancai = Column(Text)
    sucai = Column(Text)
    dayudarou = Column(Text)
    tanggeng = Column(Text)
    liangcai = Column(Text)
    suiji_candan = Column(Text)


class Caileibie(Base):
    __tablename__ = 'cai_category'
    id = Column(Integer,index=True,primary_key=True)
    category = Column(VARCHAR(10))
    category_url = Column(VARCHAR(50))


class Caidan(Base):
    __tablename__ = 'cai_menu'
    id = Column(Integer,index=True,primary_key=True)
    title = Column(VARCHAR(50))
    url = Column(VARCHAR(100))
    img_url = Column(Text)
    side_dish = Column(Text)
    stats = Column(Text)
    category_id = Column(Integer,ForeignKey('cai_category.id'))


def init_db():

    Base.metadata.create_all(DBconon().engine())

def drop_db():
    Base.metadata.drop_all(DBconon().engine())

init_db()