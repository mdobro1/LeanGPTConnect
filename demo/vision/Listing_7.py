import json
import base64
from openai import OpenAI

# encode the image
image_filename = "CarRentalSystem.jpg"
with open(f"./demo/vision/{image_filename}", "rb") as image_file:
  base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# send encoded image via OpenAI API 
response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional assistant for Software Development and Software Architecture."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Analyse class diagramm and generate C# code."},
        {"type": "text", "text": "Make output as README-markdown."},
        {"type": "text", "text": f"Architecture diagramm is stored in {image_filename}."},
        {"type": "image_url","image_url": { "url": f"data:image/jpeg;base64,{base64_image}" }},
      ]
    }
  ], max_tokens=3000
)

print(f"\n{response.choices[0].message.content}")