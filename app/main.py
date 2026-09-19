from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

load_dotenv()

from .database import Base, engine, get_db
from .models import Student
from .schemas import ChatRequest, ChatResponse
from .routers import courses, enrollments, students
from .services.chatbot.graph import build_chat_graph
from .services.vector_service import VectorService


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    db = next(get_db())
    try:
        student_records = db.query(Student).all()
        if student_records:
            VectorService().index_students(student_records)
    finally:
        db.close()

    app.state.chat_graph = build_chat_graph()
    yield


app = FastAPI(
    title="Student Database Application System",
    description=(
        "Final Year Internship Backend using FastAPI, CRUD, Gemini, "
        "LangGraph and ChromaDB."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


@app.get("/", tags=["System"])
def root():
    return {
        "project": "Student Database Application System",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health", tags=["System"])
def health():
    return {"status": "healthy"}


@app.post("/api/chat", response_model=ChatResponse, tags=["AI Chatbot"])
def chat(request: ChatRequest):
    result = app.state.chat_graph.invoke({"question": request.message})
    return ChatResponse(
        answer=result["answer"],
        sources=result.get("sources", []),
    )
