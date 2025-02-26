from fastapi import FastAPI

app = FastAPI()

@app.get("/", include_in_schema=False)
@app.head("/")
async def read_root():
    return {"message": "FastAPI is running!"}


