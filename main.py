import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    # Retrieve the PORT from Render's environment, default to 8000 if not set
    port = int(os.environ.get("PORT", 8000))

    print(f"✅ Starting FastAPI on PORT {port}")  # Debugging message

    uvicorn.run("main:app", host="0.0.0.0", port=port)
