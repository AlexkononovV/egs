from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

import os

from .config import STOCK_DB_URL 


#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user123:password123@db:5432/stock"

USER = os.environ.get('POSTGRES_USER') 
PASS = os.environ.get('POSTGRES_PASSWORD') 
DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASS}@stock-db:5432/stock"

#engine = create_async_engine(STOCK_DB_URL, echo=True, future=True)
engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
