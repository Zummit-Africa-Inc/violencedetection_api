import io
import os
import sys

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse
from PIL import Image
from model import classify_image

sys.path.append(os.path.abspath(os.path.join("..", "config")))


app = FastAPI(
    title="Violence Detection API",
    description="""An API for detecting violent actions in images.""",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
    Violence Detection API 📚
    An API for detecting violent actions in images!
    Note: add "/redoc" to get the complete documentation.
    """
    return note


@app.post("/detect-violence")
async def detect_violence(file: UploadFile = File(...)):

    contents = io.BytesIO(await file.read())
    file_bytes = np.asarray(bytearray(contents.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    cv2.imwrite("image.jpg", img)
    try:
        image = Image.open("image.jpg")
        image = image.resize((224, 224), Image.ANTIALIAS)
        image = np.array(image)
        description = classify_image(image)
        if os.path.exists("image.jpg"):
            os.remove("image.jpg")
        return description
    except ValueError:
        vals = "Error! Please upload a valid image type."
        return vals
