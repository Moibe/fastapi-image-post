from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from io import BytesIO

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/echo-image/")
async def echo_image(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        return {"error": "El archivo no es una imagen"}

    contents = await image.read()
    return StreamingResponse(BytesIO(contents), media_type=image.content_type)

@app.post("/get-mars-image/")
async def get_mars_image(text: str = Form(...)):
    image_path = "mars.png"  # Asumiendo que mars.png está en la misma carpeta que tu archivo .py
    return FileResponse(image_path, media_type="image/png")