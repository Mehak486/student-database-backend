# Student Database Application System – Backend

A final-year internship backend project built with **FastAPI, SQLAlchemy, SQLite, Pydantic, Gemini API, LangGraph, and ChromaDB**.

## 🚀 Live Application

* **Live API:** https://student-database-backend-8xj1.onrender.com/
* **Swagger API Docs:** https://student-database-backend-8xj1.onrender.com/docs
* **Health Check:** https://student-database-backend-8xj1.onrender.com/health

> The Render Free instance may take some time to wake up after inactivity.

## ✨ Features

* FastAPI modular backend architecture
* Student CRUD operations
* Course CRUD operations
* Enrollment management
* SQLAlchemy ORM with SQLite
* Automatic Swagger/OpenAPI documentation
* Gemini-powered AI chatbot
* LangGraph chatbot workflow
* ChromaDB semantic retrieval
* Health-check endpoint
* Docker deployment support
* Render deployment
* Environment-based secret management

## 🛠️ Technology Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Backend development         |
| FastAPI    | REST API framework          |
| SQLAlchemy | ORM and database operations |
| SQLite     | Database                    |
| Pydantic   | Data validation             |
| Gemini API | AI chatbot                  |
| LangGraph  | AI workflow                 |
| ChromaDB   | Vector/semantic retrieval   |
| Docker     | Containerization            |
| Render     | Cloud deployment            |

## 📁 Project Structure

```text
student-database-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   │
│   ├── routers/
│   │   ├── students.py
│   │   ├── courses.py
│   │   └── enrollments.py
│   │
│   └── services/
│       ├── gemini_service.py
│       ├── vector_service.py
│       └── chatbot/
│           └── graph.py
│
├── scripts/
│   └── seed_data.py
│
├── data/
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mehak486/student-database-backend.git
cd student-database-backend
```

### 2. Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example`:

```bash
copy .env.example .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
```

**Never commit `.env` or expose your API key.**

### 5. Seed sample data

```bash
python scripts/seed_data.py
```

### 6. Run the backend

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Local API:

```text
http://127.0.0.1:8000
```

Local Swagger:

```text
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

### Students

```text
POST   /api/students
GET    /api/students
GET    /api/students/{student_id}
PUT    /api/students/{student_id}
DELETE /api/students/{student_id}
```

### Courses

```text
POST   /api/courses
GET    /api/courses
GET    /api/courses/{course_id}
PUT    /api/courses/{course_id}
DELETE /api/courses/{course_id}
```

### Enrollments

```text
POST   /api/enrollments
GET    /api/enrollments
GET    /api/enrollments/{enrollment_id}
DELETE /api/enrollments/{enrollment_id}
```

### AI Chatbot

```text
POST /api/chat
```

Example request:

```json
{
  "message": "Which students are in Computer Science?"
}
```

The chatbot retrieves relevant student information from **ChromaDB**, processes it through **LangGraph**, and generates a response using the **Gemini API**.

## 🏗️ Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Student / Course / Enrollment APIs
   │          │
   │          ▼
   │      SQLAlchemy
   │          │
   │          ▼
   │        SQLite
   │
   └── AI Chatbot
          │
          ▼
       LangGraph
          │
          ├── ChromaDB
          │
          └── Gemini API
```

## 🐳 Docker

Build:

```bash
docker build -t student-database-backend .
```

Run:

```bash
docker run --env-file .env -p 8000:8000 student-database-backend
```

## ☁️ Deployment

The backend is deployed using **Docker + Render**.

Deployment configuration is available in:

```text
render.yaml
```

Environment secrets such as `GEMINI_API_KEY` are configured securely through the Render dashboard.

## 🔐 Security

* API keys are stored in environment variables.
* `.env` is excluded through `.gitignore`.
* Virtual environment files are excluded from Git.
* Database and ChromaDB runtime files are not committed.
* Secrets should never be hard-coded or uploaded to GitHub.

## 👩‍💻 Author

**Mehak Sharma**

B.Tech Computer Science Graduate

GitHub: https://github.com/Mehak486

