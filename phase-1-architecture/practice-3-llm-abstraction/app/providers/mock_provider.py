from app.providers.base_provider import BaseLLMProvider


class MockProvider(BaseLLMProvider):

    async def generate(self, prompt: str) -> str:

        return f"Mock LLM response to: {prompt}"