import json
import base64
from openai import OpenAI

# encode the image
with open("./demo/vision/ArchitecturePic1.jpg", "rb") as image_file:
  base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# send encoded image via OpenAI API 
response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional assistant for Cloud Architecture solutions like Azure, AWS etc.."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Analyse architecture. Make output as README-markdown."},
        {"type": "image_url","image_url": { "url": f"data:image/jpeg;base64,{base64_image}" }},
      ]
    }
  ], max_tokens=1000
)

print(f"\n{response.choices[0].message.content}")