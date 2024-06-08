from openai import OpenAI

completion = OpenAI().chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a general assistant, skills to write advanced essays."},
    {"role": "user", "content": "Tell me about capital of France."}
  ]
)

print(completion.choices[0].message.content)