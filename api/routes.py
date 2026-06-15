from fastapi import APIRouter
from pydantic import BaseModel, field_validator

router = APIRouter()


ALLOWED_SCHEMES = ("https://", "http://")


class ShortenUrlDto(BaseModel):
    url: str

    @field_validator("url")
    def validate_urls(value):
        if not value.startswith(ALLOWED_SCHEMES):
            allowed = ", ".join(ALLOWED_SCHEMES)
            raise ValueError(f"URL must start with one of: {allowed}")
        return value


@router.post("/shorten")
def shorten_url(dto: ShortenUrlDto):
    return {"short_url": dto.url}
