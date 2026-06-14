import os
import pickle
import faiss

from sentence_transformers import SentenceTransformer
from chunker import chunk_text

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_store():

    all_chunks = []

    for file in os.listdir("data"):

        if file.endswith(".txt"):

            path = os.path.join("data", file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            chunks = chunk_text(text)

            for chunk in chunks:

                all_chunks.append({"source": file, "text": chunk})

    chunk_texts = [chunk["text"] for chunk in all_chunks]

    embeddings = embedding_model.encode(chunk_texts, convert_to_numpy=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, "vectorstore/legal_index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    print("Vector store created!")

build_vector_store()