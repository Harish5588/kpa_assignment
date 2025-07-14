from pydantic import BaseModel

# request schema for creating form data
class BasicFormDataCreate(BaseModel):
    name:str
    gender:str
    mobile:str
    email:str

# response schema 
class BasicFormDataResponse(BasicFormDataCreate):
    id:int

    class Config:
        orm_mode=True
        