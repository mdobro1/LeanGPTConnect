import json
from openai import OpenAI

with open("./demo/vision/images_list.json", 'r') as file:  images_urls = json.load(file)

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional travel assistant, skilled to analyse, compare and make recommendations."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Make detailed description and comparison of the pros and cons of the given sightseens."},
        {"type": "text", "text": "Make output in German as README-markdown."},
        {"type": "image_url", "image_url": { "url": images_urls.get("London") }},
        {"type": "image_url","image_url": { "url": images_urls.get("Paris") }},
      ]
    }
  ], max_tokens=3000
)

print(f"\n{response.choices[0].message.content}")