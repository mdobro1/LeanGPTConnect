import os
import requests
import json
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
          {"type": "text", "text": "What do you see in this image?"},
          {"type": "image_url", "image_url": { "url": "https://bit.ly/img_city_1" }}
      ]
    }
  ], "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
response_data = json.loads(response.text)

print(response_data.get("choices")[0].get("message").get("content"))