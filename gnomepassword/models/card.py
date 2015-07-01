from sqlalchemy import Column, DateTime, Integer, String
from gnomepassword.models import Base


class Card(Base):
    '''Database representation of a credit card'''
    id = Column(Integer, primary_key=True)
    card_name = Column('card_name', String(200))
    name_in_card = Column('name_in_card', String(100))
    card_number = Column('card_number', String(24))
    valid = Column('valid', DateTime)
    card_code = Column('card_code', Column(10))
