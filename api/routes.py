from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

from services.shortner import generate_code

router = APIRouter()


class ShortenUrlDto(BaseModel):
    url: HttpUrl


@router.post("/shorten")
def shorten_url(dto: ShortenUrlDto):

    code = generate_code()
    return {"short_url": code}
