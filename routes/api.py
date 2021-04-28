import fastapi
from models.CipherResponse import CipherResponse
from models.CipherRequest import CipherRequest
from services.Ciphers.transposition import encode, decode


router = fastapi.APIRouter(prefix="/api/v1",)


@router.post('/encode', response_model=CipherResponse)
def encode_text(data: CipherRequest):
    result: str = encode(data.secret, data.text)
    return {"text": result}


@router.post('/decode', response_model=CipherResponse)
def decode_secret(data: CipherRequest):
    result: str = decode(data.secret, data.text)
    return {"text": result}
