from enum import Enum


class Instruments(Enum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    COHERE = "cohere"
    GOOGLE_GENERATIVEAI = "google_generativeai"
    LANGCHAIN = "langchain"
    OPENAI = "openai"
    REQUESTS = "requests"
    URLLIB3 = "urllib3"
    VERTEXAI = "vertexai"
