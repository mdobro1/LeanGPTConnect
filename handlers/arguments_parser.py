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
import argparse

#====================================
class ArgumentsParser:
#====================================
    #------------------------------------------------------------------------------------------------
    def __init__(self):
    #------------------------------------------------------------------------------------------------
        self.parser = argparse.ArgumentParser(description="Parser for handling arguments")
        self.parser.add_argument("--user-prompt", type=str, default=None, help="User prompt for the chat")
        self.parser.add_argument("--data-context", type=str, default=None, help="Data context for the chat")
        self.parser.add_argument("--model-name", type=str, default="gpt-3.5-turbo", help="LLM-Model name to use")
        self.parser.add_argument("--setup-part", type=int, default=20, help="Setup messages part percentage")
        self.parser.add_argument("--user-part", type=int, default=80, help="User messages part percentage")
    
    #------------------------------------------------------------------------------------------------
    def parse_args(self):
    #------------------------------------------------------------------------------------------------
        return self.parser.parse_args()
