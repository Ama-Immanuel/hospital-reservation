from typing import Union

from fastapi import FastAPI

from auth.router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message: Hospital Reservations API"}