import os
import openai
# from dotenv import dotenv_values
# from operator import itemgetter

# config = dotenv_values(".env")
# openai.api_key = config.get("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def justModelsIds():
    models = openai.Model.list().data
    modelsIds = [ sub['id'] for sub in models ]
    # modelsIds = list(map(itemgetter('id'), models))
    return modelsIds

def requestCompletion(text):
  return openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=text,
    max_tokens=10,
    temperature=2
  ).choices[0];
  
def requestChatCompletion(prompt, model="gpt-3.5-turbo"): 
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
      model=model, 
      messages=messages, 
      temperature=0
  )
  return response.choices[0].message