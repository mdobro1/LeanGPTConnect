'''
Example usage:

def main():
    parser = ArgumentsParser()
    args = parser.parse_args()

    print("User Prompt:", args.user_prompt)
    print("Data Context:", args.data_context)
    print("Model Name:", args.model_name)
    print("Setup Message Part in Percent:", args.setup_part)
    print("User Message Part in Percent:", args.user_part)

if __name__ == "__main__":
    main()
'''
import os
import argparse

#====================================
class ArgumentsParser:
#====================================
    #------------------------------------------------------------------------------------------------
    def __init__(self):
    #------------------------------------------------------------------------------------------------
        self.parser = argparse.ArgumentParser(description="Parser for handling arguments")
        self.parser.add_argument("--user-prompt", type=str, default=None, help="User prompt for the chat (default=None)")
        self.parser.add_argument("--data-context", type=str, default=None, help="Data context for the chat (default=None)")
        self.parser.add_argument("--model-name", type=str, default="gpt-3.5-turbo", help="LLM-Model name to use (default=\"gpt-3.5-turbo\")")
        self.parser.add_argument("--setup-part", type=int, default=20, help="Setup messages part percentage (default=20 percent)")
        self.parser.add_argument("--user-part", type=int, default=80, help="User messages part percentage (default=80 percent)")
        self.parser.add_argument("--api-key", type=str, default=os.getenv("OPENAI_API_KEY"), help="OpenAI API Key")
        self.parser.add_argument("--api-url", type=str, default=os.getenv("OPENAI_API_URL"), help="Endpoint-URL of the Azure OpenAI service")
        
        default_api_platform = os.getenv("OPENAI_API_PLATFORM")
        if not default_api_platform:
            default_api_platform = "OpenAI"
        
        self.parser.add_argument("--api-platform", type=str, default=default_api_platform, help="API-Platform - OpenAI or Azure service")
    
    #------------------------------------------------------------------------------------------------
    def parse_args(self):
    #------------------------------------------------------------------------------------------------
        return self.parser.parse_args()