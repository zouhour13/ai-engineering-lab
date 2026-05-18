def validate_message(message: str):

    if not message.strip():
        raise ValueError("Message cannot be empty")