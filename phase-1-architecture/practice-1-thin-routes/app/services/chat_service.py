
async def generate_response(message: str):

    if not message.strip():#Error Handling
        raise ValueError("Message cannot be empty")

    response = {
        "original": message,
        "lowercase": message.lower(),
        "word_count": len(message.split())
    }

    return response    