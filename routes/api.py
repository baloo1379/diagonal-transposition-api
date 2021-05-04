from fastapi import APIRouter, Depends
from schemas.ciphers import Response as CipherResponse, Request as CipherRequest
from schemas.user import User
from services.ciphers.transposition import encode, decode
from services.auth import authenticate_user


router = APIRouter(prefix="/api/v1",)


@router.get('/')
def health():
    return {"health": "ok"}


@router.post('/encode', response_model=CipherResponse)
def encode_text(data: CipherRequest, current_user: User = Depends(authenticate_user)):
    result: str = encode(data.secret, data.text)
    return {"text": result}


@router.post('/decode', response_model=CipherResponse)
def decode_secret(data: CipherRequest, current_user: User = Depends(authenticate_user)):
    result: str = decode(data.secret, data.text)
    return {"text": result}
