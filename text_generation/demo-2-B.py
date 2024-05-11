from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining different facts and concepts with creative flair."},
    {"role": "user", "content": "Tell me about capital of France."}
  ]
)

print(completion.choices[0].message.content)