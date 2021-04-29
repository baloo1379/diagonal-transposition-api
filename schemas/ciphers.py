from pydantic import BaseModel


class Request(BaseModel):
    secret: str
    text: str


class Response(BaseModel):
    text: str
