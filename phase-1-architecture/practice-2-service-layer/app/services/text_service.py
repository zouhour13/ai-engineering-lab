def process_text(message: str):

    return {
        "original": message,
        "lowercase": message.lower(),
        "word_count": len(message.split())
    }