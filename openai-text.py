from openai import OpenAI
client = OpenAI()

system_content = input("Introduce el contexto delsistema: ")
user_content = input("Introduce el prompt del usuario: ")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": system_content},
    {"role": "user", "content": user_content}
  ]
)

print(completion.choices[0].message)