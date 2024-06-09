import json
from openai import OpenAI

with open("./demo/vision/images_list.json", 'r') as file:  images_urls = json.load(file)

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining different facts and concepts with creative flair."},
    {
      "role": "user",
      "content": [
        {"type": "image_url","image_url": { "url": images_urls.get("Paris") }},
        {"type": "text", "text": "Write about what do you see."},
        {"type": "text", "text": "Write a poem in German."},
      ]
    }
  ], max_tokens=1000
)

# print & save result
result = response.choices[0].message.content
print(result)
with open(f"./demo/vision/Listing_3_Response.txt", "w", encoding="utf-8") as outfile: 
  outfile.write(result)
