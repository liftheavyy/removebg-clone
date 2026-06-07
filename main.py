from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from rembg import remove
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "RemoveBG API Running"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents))

    result = remove(image)

    result.save("output.png")

    return FileResponse(
        "output.png",
        media_type="image/png",
        filename="output.png"
    )