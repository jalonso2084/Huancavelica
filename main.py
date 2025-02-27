import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    # Retrieve the PORT from Render's environment, default to 8000 if not set
    port = os.environ.get("PORT", "NOT SET")

    print(f"✅ DEBUG: PORT from Render is: {port}")  # Debugging message

    if port == "NOT SET":
        print("⚠️ ERROR: PORT environment variable is missing! Using default port 8000.")
        port = 8000
    else:
        port = int(port)

    uvicorn.run("main:app", host="0.0.0.0", port=port)
