import json
from openai import OpenAI

with open("./demo/vision/images_list.json", 'r') as file:  images_urls = json.load(file)

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional assistant for Cloud Architecture solutions like Azure, AWS etc.."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Analyse architecture."},
        {"type": "image_url","image_url": { "url": images_urls.get("Azure-1") }},
      ]
    }
  ], max_tokens=1000
)

print(f"\n{response.choices[0].message.content}")