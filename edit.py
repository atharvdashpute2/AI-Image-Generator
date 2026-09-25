import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ["API_KEY"]

response = openai.Image.create_edit(
  image=open("images/img-dev.png", "rb"),
  mask=open("images/img-dev-mask.png", "rb"),
  prompt="a developer working on laptop near beach full frame with boat showing on screen",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)