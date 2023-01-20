
import os
import openai
openai.organization = "org-k3FtMeCql1X63YVJ9hrdjyXP"
openai.api_key_path = "key.txt"
#with open("Sample-Outputs/Model-list-output.txt", "w") as file:
  #  file.write(str(openai.Model.list()))
    
prompt = "What is AI"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

with open("Sample-Outputs/text-davinci-what-is-ai.txt", "w") as file:
   file.write(str(response))
    