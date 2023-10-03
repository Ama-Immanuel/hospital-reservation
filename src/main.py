from typing import Union

from fastapi import FastAPI

from auth.router import router as authRouter

app = FastAPI()

app.include_router(authRouter)

@app.get("/")
def home():
    return {"message: Hospital Reservations API"}