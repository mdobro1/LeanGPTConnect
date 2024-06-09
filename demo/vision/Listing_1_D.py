import os
from openai import AzureOpenAI

# Azure OpenAI endpoint like:
#  https://<MY_RESOURCE>.openai.azure.com/openai/deployments/<MY_DEPLOYMENT>/extensions"

response = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version='2023-12-01-preview',
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")).chat.completions.create(
            model="<MY_DEPLOYMENT>",
            messages=[
              {
                "role": "user",
                "content": [
                  {"type": "text", "text": "What do you see in this image?"},
                  {"type": "image_url", "image_url": { "url": "https://bit.ly/img_city_1" }}
                ]
              }
            ], max_tokens=1000
          )

print(response.choices[0].message.content)