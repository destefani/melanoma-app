import io
from numpy import bytes0
import torch
from torchvision import transforms
import streamlit as st
from PIL import Image


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

# Load model
model = torch.load('models/0020.pt')
model.eval().to('cpu')

st.title('Melanoma Detection')

uploaded_file = st.file_uploader('Upload image')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    input_image = transform_image(bytes_data)
    prediction = model(input_image)
    probability = torch.sigmoid(prediction).item()

    st.write('Malignancy Probability:')
    st.write(f'{int(probability * 100)}%')
    st.image(bytes_data)