import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "unknown")}