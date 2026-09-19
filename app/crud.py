from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


# ---------- Students ----------

def create_student(db: Session, data: schemas.StudentCreate):
    obj = models.Student(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_students(db: Session, skip=0, limit=100):
    return db.scalars(select(models.Student).offset(skip).limit(limit)).all()


def get_student(db: Session, student_id: int):
    return db.get(models.Student, student_id)


def update_student(db: Session, student_id: int, data: schemas.StudentUpdate):
    obj = get_student(db, student_id)
    if not obj:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_student(db: Session, student_id: int):
    obj = get_student(db, student_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


# ---------- Courses ----------

def create_course(db: Session, data: schemas.CourseCreate):
    obj = models.Course(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_courses(db: Session):
    return db.scalars(select(models.Course)).all()


def get_course(db: Session, course_id: int):
    return db.get(models.Course, course_id)


def update_course(db: Session, course_id: int, data: schemas.CourseUpdate):
    obj = get_course(db, course_id)
    if not obj:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_course(db: Session, course_id: int):
    obj = get_course(db, course_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


# ---------- Enrollments ----------

def create_enrollment(db: Session, data: schemas.EnrollmentCreate):
    obj = models.Enrollment(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_enrollments(db: Session):
    return db.scalars(select(models.Enrollment)).all()


def get_enrollment(db: Session, enrollment_id: int):
    return db.get(models.Enrollment, enrollment_id)


def delete_enrollment(db: Session, enrollment_id: int):
    obj = get_enrollment(db, enrollment_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
