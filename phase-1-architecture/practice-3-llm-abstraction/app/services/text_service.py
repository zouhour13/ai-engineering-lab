def process_text(message: str) -> dict:

    return {
        "processed": message.lower(),
        "word_count": len(message.split())
    }