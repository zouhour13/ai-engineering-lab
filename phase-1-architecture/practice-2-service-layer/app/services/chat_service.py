from app.services.validation_service import validate_message
from app.services.text_service import process_text

async def generate_response(message: str):

    validate_message(message)

    response = process_text(message)

    return response