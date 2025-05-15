from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
import zope.sqlalchemy

DBSession = scoped_session(sessionmaker())
zope.sqlalchemy.register(DBSession)

Base = declarative_base()

class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    npm = Column(String)
    jurusan = Column(String)
