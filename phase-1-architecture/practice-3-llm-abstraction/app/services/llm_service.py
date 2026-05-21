from app.providers.mock_provider import MockProvider

provider = MockProvider()


async def generate_llm_response(prompt: str) -> str:

    response = await provider.generate(prompt)

    return response