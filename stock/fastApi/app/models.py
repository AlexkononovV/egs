from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import ARRAY,UUID
from sqlalchemy.orm import relationship

#from database import Base
from .database import Base 
#from database import Base 

book_authors = Table('book_authors', Base.metadata,
    Column('book_id', ForeignKey('books.book_id'), primary_key=True),
    Column('author_id', ForeignKey('authors.id'), primary_key=True)
)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    books = relationship ("Book", secondary="book_authors", back_populates='authors')

'''class AuthorBook(Base):
    __tablename__='author_books'
    author_id = Column(Integer, ForeignKey('authors.id'),primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id'),primary_key=True)
'''
'''class CategoryBook(Base):
    __tablename__='category_books'
    category_id = Column(Integer, ForeignKey('categories.id'),primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id'),primary_key=True)
'''
'''class PublisherBook(Base):
    __tablename__='publisher_books'
    publisher_id = Column(Integer, ForeignKey('publishers.id'),primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id'),primary_key=True)
'''

class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, index=True)
    title =  Column(String, index=True, nullable=False)
    date = Column(Date)
    amount_in_stock = Column(Integer)
    amount_reserved = Column(Integer)
    authors = relationship("Author", secondary="book_authors",uselist=True, back_populates='books')

    #authors_id = Column(ARRAY(ForeignKey("authors.id")))
    #categories_id= Column(ARRAY(ForeignKey("categories.id")))
    #name =  Column(String, index=True)
    #publisher_id= Column(Integer,ForeignKey("publishers.id"))
    
    #publisher = Column(String, index=True)

    
    #categories = relationship("Category", back_populates="bookC")
    #orders = relationship("Order",back_populates = "bookO")
    #authors= relationship('AuthorBook', uselist=True, backref='books') #back_populates="books")
    #categories= relationship('CategoryBook',uselist=True, backref='books') #back_populates="books")
    #publisher = Column(String) #relationship("PublisherBook", backref='books')#back_populates="books")
    #orders= relationship('Order',uselist=False, backref = 'books') #, back_populates="books")
'''
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    #books = relationship ("Book",back_populates="categories")
    books = relationship ("Book", back_populates="categories")
'''
class Order(Base):
    __tablename__='orders'
  
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    requester_id = Column( Integer, ForeignKey('users.user_id'))
    status = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    complete = Column(Boolean)

    #book = relationship("Book", back_populates="orders")
    #requester = relationship("User", back_populates="orders")
    #requester = relationship("User", back_populates="orders")

'''class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    #books = relationship ("Book",back_populates="publisher")
'''

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    #orders = relationship("Order", back_populates="users")

