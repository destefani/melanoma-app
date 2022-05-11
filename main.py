
from typing import Optional
from fastapi import FastAPI, UploadFile, File
import uvicorn

from numpy import bytes0
import io
import torch
from torchvision import transforms
from PIL import Image 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
"http://localhost:3000/"
]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Load model
model = torch.load('models/0020.pt', map_location='cpu')
model.eval()

#tensor = datatype
def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.Normalize(
            mean=[0.8310, 0.6339, 0.5969],
            std=[0.1537, 0.1970, 0.2245])
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)


@app.get("/")
def hello():
    return " Mono"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    imagen = await file.read()
    input_image = transform_image(imagen)
    prediction = model(input_image)
    probability = torch.sigmoid(prediction).item()
    return {f'{int(probability * 100)}%'}
    
if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=8000)