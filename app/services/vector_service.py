import os
from pathlib import Path

import chromadb


class VectorService:
    def __init__(self):
        path = os.getenv("CHROMA_PATH", "./data/chroma")
        Path(path).mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(
            name="students",
            metadata={"description": "Student database semantic retrieval"},
        )

    def index_students(self, students):
        if not students:
            return

        ids = [str(s.id) for s in students]
        documents = [
            (
                f"Student ID: {s.id}. Name: {s.name}. Email: {s.email}. "
                f"Department: {s.department}. Semester: {s.semester}. "
                f"CGPA: {s.cgpa}. Phone: {s.phone or 'N/A'}."
            )
            for s in students
        ]

        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=[
                {"student_id": s.id, "department": s.department}
                for s in students
            ],
        )

    def search(self, query: str, n_results: int = 8) -> list[str]:
        if self.collection.count() == 0:
            return []

        result = self.collection.query(
            query_texts=[query],
            n_results=min(n_results, self.collection.count()),
        )
        return result.get("documents", [[]])[0]
