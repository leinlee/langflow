from langflow import CustomComponent
from backend.langflow.vitally.langchain.ChatOrionModel import ChatOrionModel


class ChatOrionLLM(CustomComponent):
    display_name = "ChatOrionLLM"
    description = "component for chat orion LLM"

    def build_config(self) -> dict:
        return {
            "base_url": {
                "display_name": "Base URL",
                "required": True,
                "field_type": "str",
                "value": "http://127.0.0.1:8000/v1/",
            },
        }

    def build(self, base_url: str = "http://127.0.0.1:8000/v1/") -> ChatOrionModel:
        llm = ChatOrionModel(temperature=0, model_name="orion-14b-int4", base_url=base_url)
        return llm
