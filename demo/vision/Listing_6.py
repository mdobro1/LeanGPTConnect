import json
import base64
from openai import OpenAI

# encode the image
image_filename = "ArchitecturePic1.jpg"
with open(f"./demo/vision/{image_filename}", "rb") as image_file:
  base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# send encoded image via OpenAI API 
response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional assistant for Cloud Architecture solutions like Azure, AWS etc.."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Analyse architecture."},
        {"type": "text", "text": "Make output as README-markdown."},
        {"type": "text", "text": f"Include hyperlink for Architecture diagramm stored in {image_filename}."},
        {"type": "image_url","image_url": { "url": f"data:image/jpeg;base64,{base64_image}" }},
      ]
    }
  ], max_tokens=2000
)

# print & save result
result = response.choices[0].message.content
print(result)
with open(f"./demo/vision/Listing_6_Response.md", "w", encoding="utf-8") as outfile: 
  outfile.write(result)
