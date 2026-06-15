from fastapi import FastAPI
from core.config import settings

app = FastAPI()


@app.get("/")
def root():
    return {"message": settings.APP_NAME}
