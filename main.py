import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    # Explicitly log the PORT variable for debugging
    port = os.getenv("PORT")
    if port is None:
        print("⚠️ PORT environment variable is not set! Defaulting to 8000.")
        port = 8000
    else:
        print(f"✅ Using PORT={port} from environment.")

    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
