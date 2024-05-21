# LeanGPTConnect
Demo code for OpenAI API

This project contains Python demo-code for OpenAI API

# Usage of LeanGPTConnect

python main.py [-h] [--user-prompt USER_PROMPT] [--data-context DATA_CONTEXT] [--model-name MODEL_NAME] [--setup-part SETUP_PART] [--user-part USER_PART]

Parser for handling arguments

optional arguments:
  -h, --help            show this help message and exit
  --user-prompt USER_PROMPT
                        User prompt for the chat (default=None)
  --data-context DATA_CONTEXT
                        Data context for the chat (default=None)
  --model-name MODEL_NAME
                        LLM-Model name to use (default="gpt-3.5-turbo")
  --setup-part SETUP_PART
                        Setup messages part percentage (default=20 percent)
  --user-part USER_PART
                        User messages part percentage (default=80 percent)
