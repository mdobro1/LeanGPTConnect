from openai import OpenAI

completion = OpenAI().chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining different facts and concepts with creative flair. Use German language in output."},
    {"role": "user", "content": "Tell me about capital of France."}
  ]
)

print(completion.choices[0].message.content)