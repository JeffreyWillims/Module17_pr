from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from torch.backends.quantized import engine
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///ecommerce.db", echo=True)


SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass