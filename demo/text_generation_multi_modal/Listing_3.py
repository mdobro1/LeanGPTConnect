from openai import OpenAI
import json

with open("./demo/text_generation_multi_modal/images_list.json", 'r') as file:  images_urls = json.load(file)

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining different facts and concepts with creative flair."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Write about what do you see."},
        {"type": "image_url","image_url": { "url": images_urls.get("Paris") }},
        {"type": "text", "text": "Write a poem in German."}
      ]
    }
  ], max_tokens=1000
)

print(f"\n{response.choices[0].message.content}")