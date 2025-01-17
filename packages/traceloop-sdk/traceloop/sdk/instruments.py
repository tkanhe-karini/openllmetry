from enum import Enum


class Instruments(Enum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    COHERE = "cohere"
    LANGCHAIN = "langchain"
    MISTRAL = "mistral"
    OPENAI = "openai"
    REQUESTS = "requests"
    SAGEMAKER = "sagemaker"
    URLLIB3 = "urllib3"
