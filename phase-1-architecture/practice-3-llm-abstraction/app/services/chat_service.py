from app.services.validation_service import validate_message
from app.services.text_service import process_text
from app.services.llm_service import generate_llm_response


async def generate_chat_response(message: str) -> dict:

    validate_message(message)

    text_data = process_text(message)

    llm_response = await generate_llm_response(message)

    return {
        "original": message,
        "processed": text_data["processed"],
        "llm_response": llm_response,
        "word_count": text_data["word_count"]
    }