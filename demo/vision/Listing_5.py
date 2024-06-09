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

# print & save result
result = response.choices[0].message.content
print(result)
with open(f"./demo/vision/Listing_5_Response.txt", "w", encoding="utf-8") as outfile: 
  outfile.write(result)
