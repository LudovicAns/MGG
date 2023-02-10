import requests
from datetime import datetime

url = "https://api.openai.com/v1/engines/text-curie-001/completions"
api_key = ""

question = "Dis nous quelques mots d'actualités en France (pas plus d'une phrase)."
 
headers = {
    'authorization': f"Bearer {api_key}",
    'content-type': "application/json"
    }

response = requests.request('POST', url, headers=headers, json={
  "prompt": question,
  "max_tokens": 128,
  "temperature": 0.5,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
})

from datetime import datetime

today = datetime.now()
date_str = today.strftime("%d %B %Y")

result = response.json()
answer = result["choices"][0]["text"]

lines = answer.split('\n')

new_lines = [line.strip() for line in lines if line.strip()]
new_lines.insert(0, f"{10*'='}{date_str}{10*'='}")
new_lines = new_lines + ['']

new_Answer = "\n".join(new_lines)

with open("Messages from openAI.txt", "a") as file:
  file.write(new_Answer)