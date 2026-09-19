import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dotenv import load_dotenv
load_dotenv()

from app.database import Base, SessionLocal, engine
from app.models import Course, Enrollment, Student
from app.services.vector_service import VectorService

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    if db.query(Student).count() == 0:
        students = [
            Student(
                name="Aarav Sharma",
                email="aarav@example.com",
                department="Computer Science",
                semester=8,
                cgpa=8.72,
                phone="9876500001",
            ),
            Student(
                name="Ananya Verma",
                email="ananya@example.com",
                department="Information Technology",
                semester=6,
                cgpa=9.10,
                phone="9876500002",
            ),
            Student(
                name="Rohan Kumar",
                email="rohan@example.com",
                department="Computer Science",
                semester=7,
                cgpa=7.85,
                phone="9876500003",
            ),
            Student(
                name="Priya Singh",
                email="priya@example.com",
                department="Electronics",
                semester=8,
                cgpa=8.35,
                phone="9876500004",
            ),
            Student(
                name="Vivek Yadav",
                email="vivek@example.com",
                department="Computer Science",
                semester=5,
                cgpa=7.40,
                phone="9876500005",
            ),
        ]
        db.add_all(students)

    if db.query(Course).count() == 0:
        db.add_all([
            Course(code="CS401", name="Machine Learning", credits=4),
            Course(code="CS402", name="Backend Development", credits=4),
            Course(code="CS403", name="Database Systems", credits=3),
        ])

    db.commit()

    students = db.query(Student).all()
    courses = db.query(Course).all()

    if db.query(Enrollment).count() == 0:
        db.add_all([
            Enrollment(student_id=students[0].id, course_id=courses[0].id, grade="A"),
            Enrollment(student_id=students[0].id, course_id=courses[1].id, grade="A"),
            Enrollment(student_id=students[1].id, course_id=courses[2].id, grade="A+"),
            Enrollment(student_id=students[2].id, course_id=courses[1].id, grade="B+"),
        ])
        db.commit()

    VectorService().index_students(students)
    print("Sample data inserted and indexed successfully.")

finally:
    db.close()
