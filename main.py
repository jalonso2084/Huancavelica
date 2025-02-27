from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_model=dict, methods=["GET", "HEAD"])
async def read_root():
    return {"message": "FastAPI is running!"}


