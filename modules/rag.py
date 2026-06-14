import pickle
import faiss
from langsmith import traceable
from sentence_transformers import SentenceTransformer
from langchain_google_genai import ChatGoogleGenerativeAI


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

index = faiss.read_index("vectorstore/legal_index.faiss")

with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

@traceable(name="retriever")
def retrieve(question, k=3):

    question_embedding = embedding_model.encode([question])

    distances, indices = index.search(question_embedding, k)

    results = []

    for idx in indices[0]:

        results.append(chunks[idx])

    return results

@traceable(name="generate_answer")
def answer_question(question):

    retrieved_chunks = retrieve(question)

    context = "\n\n".join(chunk["text"] for chunk in retrieved_chunks)

    prompt = f"""
        You are a legal assistant for Indian legal awareness.

        Answer using ONLY the provided context.

        When possible:
        - Mention the relevant law or act.
        - Use simple language.
        - Structure the answer with bullet points.
        - Mention penalties, rights, or provisions if relevant.

        Context:
        {context}

        Question:
        {question}
        """
    
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            chunk["source"]
            for chunk in retrieved_chunks
        ]
    }