from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .import schemas,models
from .database import SessionLocal

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/formData/saveBasicFormData", response_model=schemas.BasicFormDataResponse)
def save_basic_form_data(form: schemas.BasicFormDataCreate,db: Session=Depends(get_db)):
    db_data=models.BasicFormData(**form.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/formData/getBasicFormDataByFormId/{form_id}",response_model=schemas.BasicFormDataResponse)
def get_basic_form_data(form_id:int, db:Session=Depends(get_db)):
    form=db.query(models.BasicFormData).filter(models.BasicFormData.id==form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="fForm not found")
    return form