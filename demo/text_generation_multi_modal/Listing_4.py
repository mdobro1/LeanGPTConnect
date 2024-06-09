from openai import OpenAI
import json

with open("./demo/text_generation_multi_modal/images_list.json", 'r') as file:  images_urls = json.load(file)

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a professional travel assistant, skilled to analyse, compare and make recommendations."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Compare the pros and cons of the sightseens. Make output in German in README-markdown."},
        {"type": "image_url", "image_url": { "url": images_urls.get("London") }},
        {"type": "image_url","image_url": { "url": images_urls.get("Paris") }},
      ]
    }
  ], max_tokens=1000
)

print(f"\n{response.choices[0].message.content}")