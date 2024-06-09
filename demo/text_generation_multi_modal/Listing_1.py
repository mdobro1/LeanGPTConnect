from openai import OpenAI

response = OpenAI().chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What do you see in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://bit.ly/3RgIh7O"
          }
        }
      ]
    }
  ], max_tokens=1000
)

print(response.choices[0].message.content)