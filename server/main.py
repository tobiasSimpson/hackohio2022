import uvicorn
from fastapi import FastAPI

app = FastAPI()
global_data = {}

@app.on_event("startup")
async def startup_event():
    print("hello")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)