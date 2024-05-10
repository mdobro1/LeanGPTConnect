from openai import OpenAI

# set "OPENAI_API_KEY" environment variable first
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France",
  max_tokens=1000
)

print(response.choices[0].text.strip())