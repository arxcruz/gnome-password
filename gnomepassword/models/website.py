from sqlalchemy import Column, DateTime, Integer, PickleType, String
from gnomepassword.models import Base


class Website(Base):
    id = Column(Integer, primary_key=True)
    url = Column('url', String(512))
    forms = Column(PickleType)