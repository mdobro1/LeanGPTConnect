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