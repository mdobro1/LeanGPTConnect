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
        {"type": "image_url","image_url": { "url": f"data:image/jpeg;base64,{base64_image}" }},
        {"type": "text", "text": "Analyse class diagramm and generate C# code."},
        {"type": "text", "text": f"Include hyperlink for class diagramm stored in {image_filename}."},
        {"type": "text", "text": "Make output as README-markdown."},
      ]
    }
  ], max_tokens=4000
)

# print & save result
result = response.choices[0].message.content
print(result)
with open(f"./demo/vision/Listing_7_Response.md", "w", encoding="utf-8") as outfile: 
  outfile.write(result)
