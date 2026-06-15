from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class ShortenUrlDto(BaseModel):
    url: HttpUrl


@router.post("/shorten")
def shorten_url(dto: ShortenUrlDto):
    return {"short_url": dto.url}
