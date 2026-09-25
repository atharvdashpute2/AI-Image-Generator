from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"]
)

with open("images/img-dev.png", "rb") as image_file, \
     open("images/img-dev-mask.png", "rb") as mask_file:

    response = client.images.edit(
        model="gpt-image-1",
        image=image_file,
        mask=mask_file,
        prompt="A developer working on a laptop near a beach, full frame, with a boat visible on the screen.",
        size="1024x1024"
    )

image_data = base64.b64decode(response.data[0].b64_json)

with open("edited_developer.png", "wb") as file:
    file.write(image_data)

print("Image edited successfully!")
print("Saved as: edited_developer.png")
