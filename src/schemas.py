from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class ResponseModel(BaseModel):
    response: str
