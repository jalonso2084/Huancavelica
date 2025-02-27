import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render’s assigned PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)
