from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)
    semester: int = Field(ge=1, le=12)
    cgpa: float = Field(ge=0, le=10)
    phone: str | None = Field(default=None, max_length=30)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    email: EmailStr | None = None
    department: str | None = Field(default=None, min_length=2, max_length=100)
    semester: int | None = Field(default=None, ge=1, le=12)
    cgpa: float | None = Field(default=None, ge=0, le=10)
    phone: str | None = Field(default=None, max_length=30)


class StudentOut(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CourseBase(BaseModel):
    code: str = Field(min_length=2, max_length=30)
    name: str = Field(min_length=2, max_length=120)
    credits: int = Field(ge=1, le=10)


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    code: str | None = Field(default=None, min_length=2, max_length=30)
    name: str | None = Field(default=None, min_length=2, max_length=120)
    credits: int | None = Field(default=None, ge=1, le=10)


class CourseOut(CourseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    grade: str | None = Field(default=None, max_length=5)


class EnrollmentOut(EnrollmentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []
