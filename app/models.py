from sqlalchemy import Column,Integer,String
from .database import Base
class BicFormData(Base):
    __tablename__="basic_form_data"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    gender=Column(String)
    mobile=Column(String)
    email=Column(String)