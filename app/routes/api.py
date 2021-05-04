from fastapi import APIRouter, Depends
from app.schemas.ciphers import Response as CipherResponse, Request as CipherRequest
from app.schemas.user import User
from app.services.ciphers.transposition import encode, decode
from app.services.auth import authenticate_user


router = APIRouter(prefix="/api/v1")


@router.get('/')
def health():
    return {"health": "ok"}


@router.post('/encode', response_model=CipherResponse)
async def encode_text(data: CipherRequest, current_user: User = Depends(authenticate_user)):
    result: str = await encode(data.secret, data.text)
    return {"text": result}


@router.post('/decode', response_model=CipherResponse)
async def decode_secret(data: CipherRequest, current_user: User = Depends(authenticate_user)):
    result: str = await decode(data.secret, data.text)
    return {"text": result}
