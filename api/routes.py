from fastapi import APIRouter

router = APIRouter()


@router.post("/shorten")
def shorten_url():
    return "ok"
