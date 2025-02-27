import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Get port from Render's environment variable
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
