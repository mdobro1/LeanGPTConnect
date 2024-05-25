# LeanGPTConnect
Lean OpenAI API client.

This project contains python demo-code and lean client for OpenAI API.

# Usage of LeanGPTConnect

```sh
python lean_gpt.py [-h] [--user-prompt USER_PROMPT]
                [--data-context DATA_CONTEXT] [--model-name MODEL_NAME] 
                [--setup-part SETUP_PART] [--user-part USER_PART]
```

## (Optional) Arguments:
  + **-h, --help**                      show this help message and exit
  + **--user-prompt _<USER_PROMPT>_**       User prompt for the chat (default=None)
  + **--data-context _<DATA_CONTEXT>_**     Data context for the chat (default=None)
  + **--model-name _<MODEL_NAME>_**         LLM-Model name to use (default="gpt-3.5-turbo")
  + **--setup-part _<SETUP_PART>_**         Setup messages part percentage (default=20 percent)
  + **--user-part _<USER_PART>_**           User messages part percentage (default=80 percent)

  ## Usage examples:

+ python lean_gpt.py
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Tourism
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context /temp/chat-copilot/tourism
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry_DE
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry_DE 
                    --model-name gpt-4-turbo-preview

# OpenAI vs. Azure API clients

Although the default option for API client is OpenAI API you could easely switch to Azure API client simply by using __AzureOpenAI__ instead of __OpenAI__ client class (see examples below).

Completion example using OpenAI Client:
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())
```

Completion example using Azure Client:
```
import os
**from openai import AzureOpenAI**

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())
```

# Environment variables

You coould set environment variables 

# Links

+ [Developer Quickstart. OpenAI.com](https://platform.openai.com/docs/quickstart)
+ [Quickstart: Get started generating text using Azure OpenAI Service. Microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python)