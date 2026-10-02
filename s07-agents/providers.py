import json
import os

class BaseLLMProvider:
    def generate(self, messages: list, tools_schema: list):
        """
        Sends messages and tools to the model provider.
        Returns unified tuple: (response_message_object, tool_call_dict_or_None)
        """
        raise NotImplementedError("Subclasses must implement generate()")


# 1. OpenRouter Provider (OpenAI Compatible)
class OpenRouterProvider(BaseLLMProvider):
    def __init__(self, api_key: str = None, model: str = "openai/gpt-4o-mini"):
        from openai import OpenAI
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key or os.environ.get("OPENROUTER_API_KEY")
        )
        self.model = model

    def generate(self, messages: list, tools_schema: list):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )
        msg = response.choices[0].message
        tool_call = None
        if msg.tool_calls:
            tc = msg.tool_calls[0]
            tool_call = {
                "id": tc.id,
                "name": tc.function.name,
                "args": json.loads(tc.function.arguments)
            }
        return msg, tool_call


# 2. OpenAI Provider (Direct)
class OpenAIProvider(BaseLLMProvider):
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        from openai import OpenAI
        self.client = OpenAI(
            api_key=api_key or os.environ.get("OPENAI_API_KEY")
        )
        self.model = model

    def generate(self, messages: list, tools_schema: list):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )
        msg = response.choices[0].message
        tool_call = None
        if msg.tool_calls:
            tc = msg.tool_calls[0]
            tool_call = {
                "id": tc.id,
                "name": tc.function.name,
                "args": json.loads(tc.function.arguments)
            }
        return msg, tool_call
