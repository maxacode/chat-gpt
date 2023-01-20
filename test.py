
import os
import openai
openai.organization = "org-k3FtMeCql1X63YVJ9hrdjyXP"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())