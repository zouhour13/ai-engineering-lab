from app.providers.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    async def generate(self, prompt: str) -> str:

        return f"Simulated OpenAI response to: {prompt}"