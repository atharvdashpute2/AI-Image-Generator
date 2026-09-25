from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"]
)

response = client.images.generate(
    model="gpt-image-1",
    prompt="A developer working on a laptop near a beach, full frame, with a boat near the beach",
    size="1024x1024"
)

image_data = base64.b64decode(response.data[0].b64_json)

with open("developer_beach.png", "wb") as file:
    file.write(image_data)

print("Image generated successfully!")
print("Saved as: developer_beach.png")
