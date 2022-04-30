from typing import List, Optional

from pydantic import BaseModel


from datetime import date 


class Author(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode = True

class Category(BaseModel):

    id: int
    name: str
    class Config:
        orm_mode = True
'''class Publisher(BaseModel):

    id: int
    name: str
    class Config:
        orm_mode = True
'''
class User(BaseModel):

    user_id: Optional[int] 
    email: Optional[str] 
    name: Optional[str] 
    class Config:
        orm_mode = True



class Order(BaseModel):

    id: int
    book_id: int
    requester_id: int
    status: Optional[str] 
    begin_date: Optional[date] 
    end_date: Optional[date] 
    complete: Optional[bool] 
    class Config:
        orm_mode = True


class Book(BaseModel):

    book_id: int
    name: str
    date: Optional[date] 
    amount_in_stock: int
    amount_reserved: int
    publisher: Optional[str] 
    authors: List[Author]
    categories: List[Category]
    
    orders: Optional[List[Order]]
    class Config:
        orm_mode = True



    #edition: Optional[str] 

    


class ApiResponse(BaseModel):

    code: Optional[int] 
    type: Optional[str] 
    message: Optional[str] 
    class Config:
        orm_mode = True
