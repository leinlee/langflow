from typing import Optional

from langchain_community.embeddings import BedrockEmbeddings
from langchain.embeddings.base import Embeddings
from langflow import CustomComponent


class AmazonBedrockEmeddingsComponent(CustomComponent):
    """
    A custom component for implementing an Embeddings Model using Amazon Bedrock.
    """

    display_name: str = "Amazon Bedrock Embeddings"
    description: str = "Embeddings model from Amazon Bedrock."
    documentation = "https://python.langchain.com/docs/modules/data_connection/text_embedding/integrations/bedrock"
    beta = True

    def build_config(self):
        return {
            "model_id": {
                "display_name": "Model Id",
                "options": ["amazon.titan-embed-text-v1"],
            },
            "credentials_profile_name": {"display_name": "Credentials Profile Name"},
            "endpoint_url": {"display_name": "Bedrock Endpoint URL"},
            "region_name": {"display_name": "AWS Region"},
            "code": {"show": False},
        }

    def build(
        self,
        model_id: str = "amazon.titan-embed-text-v1",
        credentials_profile_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        region_name: Optional[str] = None,
    ) -> Embeddings:
        try:
            output = BedrockEmbeddings(
                credentials_profile_name=credentials_profile_name,
                model_id=model_id,
                endpoint_url=endpoint_url,
                region_name=region_name,
            )  # type: ignore
        except Exception as e:
            raise ValueError("Could not connect to AmazonBedrock API.") from e
        return output
