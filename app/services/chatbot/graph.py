from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from ..gemini_service import GeminiService
from ..vector_service import VectorService


class ChatState(TypedDict, total=False):
    question: str
    context: str
    sources: list[str]
    answer: str


def build_chat_graph():
    vector = VectorService()

    def retrieve(state: ChatState):
        docs = vector.search(state["question"])
        return {
            "context": "\n".join(docs) if docs else "No matching student records found.",
            "sources": docs,
        }

    def generate(state: ChatState):
        gemini = GeminiService()
        answer = gemini.answer(state["question"], state["context"])
        return {"answer": answer}

    graph = StateGraph(ChatState)
    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)
    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()
