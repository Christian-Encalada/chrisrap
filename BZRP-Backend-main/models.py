from sqlalchemy import Column, Integer, VARCHAR
from database import Base


class Session(Base):
    __tablename__ = "sesiones"
    id = Column(Integer, primary_key=True)
    session = Column(VARCHAR)
    name = Column(VARCHAR)
    image = Column(VARCHAR)
    url = Column(VARCHAR)