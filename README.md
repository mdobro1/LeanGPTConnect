# LeanGPTConnect
Demo code for OpenAI API

This project contains Python demo-code for OpenAI API

# Usage of LeanGPTConnect

```sh
python lean_gpt.py [-h] [--user-prompt USER_PROMPT]
                [--data-context DATA_CONTEXT] [--model-name MODEL_NAME] 
                [--setup-part SETUP_PART] [--user-part USER_PART]
```

## (Optional) Arguments:
  + **-h, --help**                      show this help message and exit
  + **--user-prompt __USER_PROMPT__**       User prompt for the chat (default=None)
  + **--data-context __DATA_CONTEXT__**     Data context for the chat (default=None)
  + **--model-name __MODEL_NAME__**         LLM-Model name to use (default="gpt-3.5-turbo")
  + **--setup-part __SETUP_PART__**         Setup messages part percentage (default=20 percent)
  + **--user-part __USER_PART__**           User messages part percentage (default=80 percent)

  ## Usage examples:

