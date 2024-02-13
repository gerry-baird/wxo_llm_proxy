from pydantic import BaseModel

class LLM_Request(BaseModel):
    prompt: str
    model_id: str
    max_new_tokens: int
    min_new_tokens: int
    decoding_method: str


class LLM_Response(BaseModel):
    message: str


class LLM_Cache_Entry(BaseModel):
    request: LLM_Request
    response: LLM_Response

class Message(BaseModel):
    message: str