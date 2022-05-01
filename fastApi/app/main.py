from typing import List,Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from . import crud, models, schemas

from .database import SessionLocal, engine
#import database

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

async def db() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as db:
        yield db


# Dependency
'''def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''


#init_db()

###############____BOOKS___#############################################

@app.get('/v1/books')#, response_model=List[schemas.Book])
async def read_books(db=Depends(db), title: Optional[str] = None, author:Optional[str]=None):
    books = await crud.get_books(db, title=title, author=author)
    if books is None:
        raise HTTPException(status_code=404, detail="Books not found")
    
    return books

@app.get('/v1/book/{bookId}')#, response_model=List[schemas.Book])
async def read_book( bookId: int,db=Depends(db)):
    book = await crud.get_book_id(db, id=bookId)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post('/v1/books')
#def save_books(db=Depends(db), book_id: int, name: str,mount_in_stock:int, amount_reserved: int,date:Optional[str], authors: List[schemas.Author], categories:List[schemas.Category], orders: Optional[List[schemas.Order]] ):
async def post_book(book: schemas.BookSchema,db=Depends(db)):
    #book = crud.save_book(db, book)
    print(book)
    book2 = await crud.save_book(db, book)
    print(book2)
    if book2 is None:
        raise HTTPException(status_code=404, detail="Unknown Author id")
    return book2

@app.delete('/v1/book/{bookId}' )
def delete_book(bookId:int,db=Depends(db)):
    msg = crud.delete_book(db, bookId)
    return msg

@app.get('/v1/book/{bookId}/availability', response_model=List[schemas.BookSchema])
def read_book(bookId: int, db=Depends(db)):
    book = crud.get_book_id(db, bookId)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books.amount_in_stock

##########################____ORDERS________#################################

@app.get('/v1/order/{orderId}', response_model=List[schemas.Order])
def read_order( orderId: int, db=Depends(db)):
    order = crud.get_order_id(db, orderId)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return order

@app.get('/v1/orders', response_model=List[schemas.Order])
def read_orders( book_id: Optional[int] =None, book_title: Optional[str]=None, requester: Optional[int]=None, status:Optional[str]=None,begin_date:Optional[str]=None,end_date:Optional[str]=None, db=Depends(db),):
    order = crud.get_orders(db, book_id,book_title, requester, status, begin_date, end_date)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return order

############################__AUTHORS___########################################################

@app.post('/v1/author')
async def post_author(author: schemas.AuthorBase,db=Depends(db)):
    return await crud.save_author(db, author)

@app.get('/v1/author')#, response_model=schemas.Author)
async def get_author(id: Optional[int] =None, name: Optional[str]=None,db=Depends(db)):
    return await crud.get_author(db, name, id)

@app.delete('/v1/author/{id}' )
async def delete_book(id:int,db=Depends(db)):
    msg = await crud.delete_author(db, id)
    return msg

#############################__CATEGORIES___#####################################################
'''
@app.post('/v1/category') #, response_model=schemas.Category)
async def post_category(cat: schemas.Category,db=Depends(db)):

    return await crud.save_category(db, cat)

@app.get('/v1/category') #, response_model=List[schemas.Category])
async def get_category(id: Optional[int] =None, name: Optional[str]=None,db=Depends(db)):
    return await crud.get_category(db, name, id)

@app.delete('/v1/category/{id}' )
async def delete_book(id:int,db=Depends(db)):
    msg = await crud.delete_category(db, id)
    return msg
'''