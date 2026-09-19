# Student Database Application System – Backend

A final-year internship backend project built with **FastAPI**, **SQLAlchemy/SQLite**, **Pydantic**, **Gemini API**, **LangGraph**, and **ChromaDB**.

## Features

- Modular FastAPI architecture
- Student CRUD APIs
- Course CRUD APIs
- Enrollment CRUD APIs
- SQLite database with SQLAlchemy ORM
- Automatic Swagger/OpenAPI documentation
- Gemini-powered AI chatbot
- LangGraph chatbot workflow
- Student database interaction through natural-language questions
- ChromaDB vector database for semantic retrieval
- Health-check endpoint
- Docker deployment support
- Render deployment configuration
- Environment-variable based secrets

## Project Structure

```text
student-database-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── students.py
│   │   ├── courses.py
│   │   └── enrollments.py
│   └── services/
│       ├── __init__.py
│       ├── gemini_service.py
│       ├── vector_service.py
│       └── chatbot/
│           ├── __init__.py
│           └── graph.py
├── scripts/
│   └── seed_data.py
├── data/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

## 1. Create and activate virtual environment

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Configure Gemini

Create `.env` from `.env.example`:

```powershell
copy .env.example .env
```

Open `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not upload `.env` to GitHub.

## 4. Start the API

```powershell
uvicorn app.main:app --reload --port 8000
```

Open:

- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 5. Seed sample data

With the server stopped or in another terminal:

```powershell
python scripts/seed_data.py
```

The script inserts sample courses, students and enrollments and indexes student information into ChromaDB.

## Main API endpoints

### Students

- `POST /api/students`
- `GET /api/students`
- `GET /api/students/{student_id}`
- `PUT /api/students/{student_id}`
- `DELETE /api/students/{student_id}`

### Courses

- `POST /api/courses`
- `GET /api/courses`
- `GET /api/courses/{course_id}`
- `PUT /api/courses/{course_id}`
- `DELETE /api/courses/{course_id}`

### Enrollments

- `POST /api/enrollments`
- `GET /api/enrollments`
- `GET /api/enrollments/{enrollment_id}`
- `DELETE /api/enrollments/{enrollment_id}`

### AI Chatbot

`POST /api/chat`

Example:

```json
{
  "message": "Show me the students in Computer Science with CGPA above 8"
}
```

The chatbot uses a LangGraph workflow:

```text
User Question
     ↓
Retrieve student context from ChromaDB
     ↓
Build grounded prompt
     ↓
Gemini generates answer
     ↓
Response
```

## Vector database research/selection

This project uses **ChromaDB** because it is simple to run locally, Python-friendly, open-source, and suitable for a student-project semantic retrieval layer. The application keeps SQLite as the source of truth for structured student records and uses ChromaDB as the retrieval/index layer.

Alternatives researched for this type of project include:

| Vector DB | Typical strength | Project fit |
|---|---|---|
| ChromaDB | Simple local setup and Python integration | Selected |
| FAISS | Fast local similarity search library | Good for prototypes |
| Qdrant | Full vector database with filtering | Strong production option |
| Pinecone | Managed cloud vector database | Good managed option |
| Weaviate | Full-featured vector search platform | Good for larger systems |

## Architecture

```text
Client
  |
  v
FastAPI
  |
  +--> Routers --> CRUD --> SQLAlchemy --> SQLite
  |
  +--> Chat Router
          |
          v
       LangGraph
          |
          +--> ChromaDB retrieval
          |
          +--> Gemini API
          |
          v
       AI response
```

## Docker

Build:

```powershell
docker build -t student-database-backend .
```

Run:

```powershell
docker run --env-file .env -p 8000:8000 student-database-backend
```

## Deploying

The included `render.yaml` can be used as a starting point for Render deployment. Add `GEMINI_API_KEY` as a secret/environment variable in the deployment dashboard.

## Important

- Never commit `.env`.
- Never hard-code API keys.
- The chatbot is grounded using retrieved database information, but AI responses should still be verified for important administrative decisions.
