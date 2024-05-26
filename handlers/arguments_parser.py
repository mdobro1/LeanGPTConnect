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
        
        default_api_platform = os.getenv("OPENAI_API_PLATFORM")
        if not default_api_platform:
            default_api_platform = "OpenAI"        
        self.parser.add_argument("--api-platform", type=str, default=default_api_platform, \
                                 help="API-Platform - OpenAI or Azure service (default=\"OPENAI_API_PLATFORM\" environment variable or \"OpenAI\")")
        
        default_api_version = "2024-02-01"
        api_key_help="Original OpenAI API Key or Azure OpenAI service API Key (default=)"           
        api_endpoint_help="Endpoint-URL of the Azure OpenAI service (relevant for Azure: default=\"AZURE_OPENAI_ENDPOINT\" environment variable)"
        api_vesrion_help=f"Version of the Azure OpenAI service (relevant for Azure: default=\"{default_api_version}\")"             

        # get params for Azure OpenAI API
        default_api_key = os.getenv("OPENAI_API_KEY")
        if not default_api_key:
            default_api_key = os.getenv("AZURE_OPENAI_API_KEY")

        self.parser.add_argument("--api-key", type=str, default=default_api_key, help=api_key_help)            
        self.parser.add_argument("--api-url", type=str, default=os.getenv("AZURE_OPENAI_ENDPOINT"), help=api_endpoint_help)  
        self.parser.add_argument("--api-version", type=str, default=default_api_version, help=api_vesrion_help)               

    #------------------------------------------------------------------------------------------------
    def parse_args(self):
    #------------------------------------------------------------------------------------------------
        return self.parser.parse_args()