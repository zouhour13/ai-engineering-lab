from app.services.similarity_service import compare_texts

text1 = "Artificial intelligence is transforming healthcare."
text2 = "AI is changing modern medicine."

result = compare_texts(text1, text2)

print(result)