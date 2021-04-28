from pydantic import BaseModel


class CipherRequest(BaseModel):
    secret: str
    text: str
