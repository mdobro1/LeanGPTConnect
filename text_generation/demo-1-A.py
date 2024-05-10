from openai import OpenAI
import os

my_api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=my_api_key)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())