from sqlalchemy.orm import Session
from . import schemas
from . import models
import array 
from sqlalchemy.future import select
from sqlalchemy import delete

async def get_books(db:Session, title: str=None, author: str = None, category:str = None):
    #return db.query(models.Book).filter(models.Book.title == title).filter(models.Book.categories_id == category).filter(models.Book.authors_id == author)
    
    #books = db.query(models.Book).all()
    books = await db.execute(select(models.Book))
    
    if title is not None:
        books=books.filter(models.Book.title == title)
    if author is not None:
        books = books.filter(models.Book.authors_id == author)
    if category is not None:
        books = books.filter(models.Book.categories_id == category)

    return books.scalars().all() #books #.all()
    
async def get_book_id(db:Session, id :int=None ):
    if id is None:
        return db.query(models.Book).all()
    else:
        return db.query(models.Book).filter(models.Book.book_id==id)


async def save_book(db: Session, info: schemas.Book):
    book = models.Book(**info.dict())
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book

async def delete_book(db: Session, id:int):
    db.query(models.Book).filter(models.Book.book_id==id).delete()
    await db.commit()
    return 

def udpate_book( db:Session, id:int, stock:int, booked:int, name:str=""):
    b = db.query(models.Book).filter(models.Book.book_id==id)
    record = b.one()
    if stock is not None:
        record.amount_in_stock = stock
    if booked is not None:
        record.amount_reserved = booked
    if name is not "":
        record.name = name
    db.commit()

##########################

def get_order_id(db:Session, id :int=None ):
    if id is None:
        return db.query(models.Order).all()
    else:
        return db.query(models.Order).filter(models.Order.id==id)

def get_orders(db:Session, book_id: int = None, book_title: str =None, requester: int = None,status: str=None, begin_date: str=None, end_date: str=None):
    
    orders = db.query(models.Order).all()
    if book_id is not None:
        orders=orders.filter(models.Order.book_id == book_id)
    if book_title is not None:
        orders=orders.filter(models.Order.book_id == book_id)
    if requester is not None:
        orders=orders.filter(models.Order.requester_id == requester)
    if status is not None:
        orders=orders.filter(models.Order.status == status)
    if begin_date is not None:
        orders=orders.filter(models.Order.begin_date == begin_date)
    if end_date is not None:
        orders=orders.filter(models.Order.end_date == end_date)
    return orders

def save_order(db: Session, info: schemas.Order):
    order = models.Order(**info.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def delete_order(db: Session, id:int):
    db.query(models.Order).filter(models.Order.id==id).delete()
    db.commit()
    return 

################################

async def save_author(db: Session, info: schemas.Author):
    author = models.Author(**info.dict())
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return author

async def delete_author(db: Session, id:int):
    #db.query(models.Author).filter(models.Author.id==id).delete()
    #author = db.execute(select(models.Author).where(models.Author.id==id))
    #author = author.scalar_one()
    #await db.delete(author)
    query = delete(models.Author).where(models.Author.id == id)
    await db.execute(query)
    await db.commit()
    return "Deleted Successfully"

async def get_author(db:Session, name: str = None, id: int =None):
    authors = await db.execute(select(models.Author)) #db.query(models.Author).all()
    if name is not None:
        authors = db.query(models.Author).filter(models.Author.name == name)
    if id is not None:
        authors = db.query(models.Author).filter(models.Author.id == id)
    authors = authors.scalars().all()
    return [schemas.Author(id=a.id,name=a.name) for a in authors]
############################

def get_category(db:Session, name: str = None, id: int =None):
    cat= db.query(models.Category).all()
    if name is not None:
        cat= db.query(models.Category).filter(models.Category.name == name)
    if id is not None:
        cat=  db.query(models.Category).filter(models.Category.id == id)
    return cat
def save_category(db: Session, info: schemas.Category):
    cat = models.Category(**info.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def delete_category(db: Session, id:int):
    db.query(models.Category).filter(models.Category.id==id).delete()
    db.commit()
    return "Deleted Successfully"

#######################################
'''def get_publisher(db:Session, name: str = "", id: int =None):
    if id is None:
        return db.query(models.Publisher).filter(models.Publisher.name == name)
    else:
        return db.query(models.Publisher).filter(models.Publisher.id == id)
'''