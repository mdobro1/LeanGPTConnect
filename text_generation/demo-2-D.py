from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair. Use German language in output."},
    {"role": "user", "content": "Tell me about capital of France."}
  ]
)

print(completion.choices[0].message.content)