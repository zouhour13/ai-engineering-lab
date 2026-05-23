from app.services.embedding_service import generate_embedding
from app.utils.cosine_similarity import compute_similarity


def compare_texts(text1: str, text2: str):

    embedding1 = generate_embedding(text1)
    embedding2 = generate_embedding(text2)

    similarity = compute_similarity(embedding1, embedding2)

    return {
        "text1": text1,
        "text2": text2,
        "similarity_score": float(similarity)
    }