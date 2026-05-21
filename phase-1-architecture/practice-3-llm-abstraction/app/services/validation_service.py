def validate_message(message: str) -> None:

    if not message.strip():
        raise ValueError("Message cannot be empty")