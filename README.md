# LeanGPTConnect
Lean OpenAI API client.

This project contains python demo-code and lean client for OpenAI API.

## Usage of LeanGPTConnect

```sh
python lean_gpt.py [-h] [--user-prompt USER_PROMPT]
                [--data-context DATA_CONTEXT] [--model-name MODEL_NAME] 
                [--setup-part SETUP_PART] [--user-part USER_PART]
                [--api-key API-KEY] [--api-url ENDPOINT_URL]
                [--api-platform OpenAI | Azure]
```

## (Optional) Arguments:
  + **-h, --help**                            show this help message and exit
  + **--user-prompt _<USER_PROMPT | Batch-Prompts as JSON-filepath>_**  User prompt for the chat (default=None) or path to Batch-Prompts as JSON-file
  + **--data-context _<DATA_CONTEXT>_**       Data context for the chat (default=None)
  + **--model-name _<MODEL_NAME>_**           Model name to use or deployment name of the OpenAI service in Azure (default="gpt-3.5-turbo")
  + **--setup-part _<SETUP_PART>_**           Setup messages part percentage (default=20 percent)
  + **--user-part _<USER_PART>_**             User messages part percentage (default=80 percent)
  + **--api-key _<API-KEY>_**                 OpenAI API Key (default=OPENAI_API_KEY or AZURE_OPENAI_API_KEY environment variable)
  + **--api-url _<AZURE-OPENAI-ENDPOINT>_**   Endpoint-URL of the Azure OpenAI service (relevant for Azure: default=AZURE_OPENAI_ENDPOINT environment variable)
  + **--api-version _<API-VERSION>_**         Version of Azure OpenAI service (relevant for Azure: default="2024-02-01")
  + **--api-platform _OpenAI | Azure_**       API-Platform - OpenAI or Azure service (default=OPENAI_API_PLATFORM environment variable or "OpenAI")

  Notification: 
  
  + Instead of _api-key_, _api-url_ and _api-platform_ command-line parameters you could also respectively use **OPENAI_API_KEY**/**AZURE_OPENAI_API_KEY**, **AZURE_OPENAI_ENDPOINT** and **OPENAI_API_PLATFORM** environment variables (see Chatpter ["Environment variables"](https://github.com/mdobro1/LeanGPTConnect?tab=readme-ov-file#environment-variables) below). 
  + If both **OPENAI_API_KEY** and **AZURE_OPENAI_API_KEY** environment variables are set **OPENAI_API_KEY** will be used as default value. Use explicit _api-key_, _api-url_ and _api-platform_ arguments if you'd like to use both API plattforms in the same environment.
  
  ***Arguments _api-key_, _api-url_ and _api-platform_ have higher priority and (if given) do override corresponding values of the environment variables.***

## Usage examples:

+ python lean_gpt.py
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Tourism
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context /temp/chat-copilot/tourism
+ python lean_gpt.py --user-prompt "./batch_prompts/user_prompts_travel.json" --data-context Travel
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry_DE
+ python lean_gpt.py --user-prompt "Tell me about Paris" --data-context Poetry_DE 
                     --model-name gpt-4-turbo-preview

## OpenAI vs. Azure API clients

Although the default option for API client is OpenAI API you could easely switch to Azure API client simply by using __AzureOpenAI__ instead of __OpenAI__ client class (see examples below).

Completion example using **OpenAI** client:
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

Completion example using **Azure** client:
```
import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

# you could also use custom name you chose 
# for your deployment when you deployed a model. 
my_openai_model = "gpt-35-turbo-instruct"

response = client.completions.create(
  model=my_openai_model,
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())
```

## Environment variables

You could set following environment variables:

+ for OpenAI client - **OPENAI_API_KEY** - for OpenAI API key.
+ for Azure client - **AZURE_OPENAI_API_KEY** and **AZURE_OPENAI_ENDPOINT** - for respecitvely API key and api-url of your Azure OpenAI-Service.
+ for API Plattform - **OPENAI_API_PLATFORM**=_'OpenAI'_ or _'Azure'_ for respectively OpenAI or Azure as API platform.

Notifications: 

+ Instead of **OPENAI_API_KEY**/**AZURE_OPENAI_API_KEY**, **AZURE_OPENAI_ENDPOINT** and **OPENAI_API_PLATFORM** environment variables you could also respectively use _api-key_, _api-url_ and _api-platform_ arguments (command-line parameters, see Chatpter ["Arguments"](https://github.com/mdobro1/LeanGPTConnect?tab=readme-ov-file#optional-arguments) above). 
+ If both **OPENAI_API_KEY** and **AZURE_OPENAI_API_KEY** environment variables are set **OPENAI_API_KEY** will be used as default value. Use explicit _api-key_, _api-url_ and _api-platform_ arguments if you'd like to use both API plattforms in the same environment.

***Arguments _api-key_, _api-url_ and _api-platform_ have higher priority and (if given) do override corresponding values of the environment variables.***

Then i.e. the OpenAI client intitialization could look even simpler:

```
from openai import OpenAI

client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)
```

## Batch prompts

If _user-prompt_-parameter contains path to Batch-Prompts as JSON-file, then OpenAI-API will be run in batch mode for each of the user-prompts from the JSON batch file (see example below).

Example of the batch prompts:
```
  python lean_gpt.py --user-prompt "./batch_prompts/user_prompts_travel.json" --data-context Travel
```

Example of the batch prompt JSON-file user_prompts_travel.json:
```
{
    "prompts": [
        "How can I ensure security in my microservices architecture?",
        "What authentication mechanisms are recommended for microservices?",
        "How can I implement authorization in a microservices environment?",
        "Can you provide examples of encryption techniques suitable for microservices communication?",
        "What are some best practices for securing REST APIs in a microservices architecture?",
        "How can I protect sensitive data stored in microservices databases?"
    ]
}				
```

## Links

+ [Developer Quickstart. OpenAI.com](https://platform.openai.com/docs/quickstart)
+ [Quickstart: Get started generating text using Azure OpenAI Service. Microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python)
+ [API Reference. OpenAI.com](https://platform.openai.com/docs/api-reference/introduction)
+ [Azure OpenAI Service REST API reference. Microsoft.com](https://platform.openai.com/docs/api-reference/introduction)
+ [Azure OpenAI Service documentation. Microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
