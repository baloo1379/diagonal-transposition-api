from pydantic import BaseModel


class CipherResponse(BaseModel):
    text: str
