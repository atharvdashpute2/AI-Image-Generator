from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"]
)

with open("images/img-dev.png", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-1",
        image=image_file,
        prompt="Create a new variation of this image while keeping the main subject and composition similar."
    )

image_data = base64.b64decode(response.data[0].b64_json)

with open("images/img-dev-variation.png", "wb") as file:
    file.write(image_data)

print("Image variation generated successfully!")
