from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RootResponse(BaseModel):
    message: str

@app.get("/", response_model=RootResponse)
def read_root():
    return {"message": "FastAPI is running!"}
