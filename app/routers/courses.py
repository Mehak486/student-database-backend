from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/api/courses", tags=["Courses"])


@router.post("", response_model=schemas.CourseOut, status_code=201)
def create_course(data: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, data)


@router.get("", response_model=list[schemas.CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)


@router.get("/{course_id}", response_model=schemas.CourseOut)
def read_course(course_id: int, db: Session = Depends(get_db)):
    obj = crud.get_course(db, course_id)
    if not obj:
        raise HTTPException(404, "Course not found")
    return obj


@router.put("/{course_id}", response_model=schemas.CourseOut)
def update_course(course_id: int, data: schemas.CourseUpdate, db: Session = Depends(get_db)):
    obj = crud.update_course(db, course_id, data)
    if not obj:
        raise HTTPException(404, "Course not found")
    return obj


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    if not crud.delete_course(db, course_id):
        raise HTTPException(404, "Course not found")
    return {"message": "Course deleted successfully"}
