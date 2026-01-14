from enum import Enum


class Instruments(Enum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    COHERE = "cohere"
    GOOGLE_GENERATIVEAI = "google_generativeai"
    LANGCHAIN = "langchain"
    MCP = "mcp"
    OPENAI = "openai"
    OPENAI_AGENTS = "openai_agents"
    REQUESTS = "requests"
    SAGEMAKER = "sagemaker"
    TRANSFORMERS = "transformers"
    URLLIB3 = "urllib3"
    VERTEXAI = "vertexai"