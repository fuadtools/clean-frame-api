from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import requests
import os

app = FastAPI()

CLIPDROP_API_KEY = os.getenv("CLIPDROP_API_KEY")

@app.post("/clean-frame")
async def clean_frame(file: UploadFile = File(...)):
    image = await file.read()

    r = requests.post(
        "https://api.clipdrop.co/cleanup/v1",
        headers={"x-api-key": CLIPDROP_API_KEY},
        files={"image_file": image},
        timeout=60
    )

    if r.status_code != 200:
        return {"error": "AI processing failed"}

    return Response(content=r.content, media_type="image/png")
