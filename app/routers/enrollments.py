from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/api/enrollments", tags=["Enrollments"])


@router.post("", response_model=schemas.EnrollmentOut, status_code=201)
def create_enrollment(data: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    if not crud.get_student(db, data.student_id):
        raise HTTPException(404, "Student not found")
    if not crud.get_course(db, data.course_id):
        raise HTTPException(404, "Course not found")
    return crud.create_enrollment(db, data)


@router.get("", response_model=list[schemas.EnrollmentOut])
def list_enrollments(db: Session = Depends(get_db)):
    return crud.get_enrollments(db)


@router.get("/{enrollment_id}", response_model=schemas.EnrollmentOut)
def read_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    obj = crud.get_enrollment(db, enrollment_id)
    if not obj:
        raise HTTPException(404, "Enrollment not found")
    return obj


@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    if not crud.delete_enrollment(db, enrollment_id):
        raise HTTPException(404, "Enrollment not found")
    return {"message": "Enrollment deleted successfully"}
