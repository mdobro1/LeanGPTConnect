import os
from datetime import datetime
from openai import OpenAI
from handlers.message import Message
from handlers.batch_prompt import BatchPrompt
from handlers.token_count import TokenCounter
from handlers.model_info import ModelInfoHandler

#====================================
class CopilotHandler:
#====================================
    #------------------------------------------------------------------------------------------------
    def __init__(self, run_arguments):
    #------------------------------------------------------------------------------------------------
        self.run_arguments = run_arguments

    #------------------------------------------------------------------------------------------------
    def run(self):
    #------------------------------------------------------------------------------------------------
        self.main( \
            self.run_arguments.user_prompt, \
            self.run_arguments.data_context, \
            self.run_arguments.model_name, \
            self.run_arguments.setup_part, \
            self.run_arguments.user_part)

    #------------------------------------------------------------------------------------------------
    def main(self, prompt : str = None, message_context=None, model_name="gpt-3.5-turbo", \
            setup_message_part_in_percent = 20, user_message_part_in_percent = 80):
    #------------------------------------------------------------------------------------------------
        # init
        setup_messages = []
        user_messages = []
        user_prompts = []
        model_info : ModelInfoHandler = ModelInfoHandler("models/models_info.json")
        max_tokens = model_info.get_token_count(model_name)
        max_tokens_per_message_user = int(max_tokens / 100 * user_message_part_in_percent)
        max_tokens_per_message_setup = int(max_tokens / 100 * setup_message_part_in_percent)

        # append user prompt(s)
        if not prompt or len(prompt.strip()) < 1: 
            # interactive prompt mode
            user_prompts.append(input("Enter your prompt: "))
        else:
            if not ".json" in prompt.lower():
                # CLI prompt mode
                user_prompts.append(prompt)
            else:
                batch_prompt_file = prompt
                if not os.path.exists(batch_prompt_file):
                    raise FileNotFoundError(f"Batch file {batch_prompt_file} does not exist!")  

                # batch prompt mode
                batch_prompt = BatchPrompt(batch_prompt_file)
                for prompt_item in batch_prompt.read_prompts(): 
                    user_prompts.append(prompt_item)
        
        # get data dir
        data_directory = None
        if message_context: 
            data_directory = os.path.join("data", message_context)    
            if not os.path.exists(data_directory):
                os.makedirs(data_directory)

        # get chat files paths
        user_chat_file = f"user_chat.json"
        setup_chat_file = f"setup_chat.json"
        if data_directory: 
            user_chat_path = os.path.join(data_directory, user_chat_file)
            setup_chat_path = os.path.join(data_directory, setup_chat_file)
        else: 
            user_chat_path = user_chat_file
            setup_chat_path = setup_chat_file

        # process user messages
        for user_prompt in user_prompts:
            #------------------------------------------------------------------------------------------------
            user_messages.clear()
            user_message = Message(role="user", content=user_prompt)
            user_messages.append(user_message)
            print(f"\n---------------------------\nUser prompt: {user_prompt}")
            
            if not os.path.exists(user_chat_path):
                # create chat file if not exists with very first user message
                Message.save_to_json(user_messages, user_chat_file, data_directory)
            else:
                # load existing messages and add new user messages
                user_messages = Message.load_from_json(user_chat_file, data_directory) + user_messages

            # load existing setup messages
            if os.path.exists(setup_chat_path):
                setup_messages = Message.load_from_json(setup_chat_file, data_directory)

            # limit setup messages by max token count 
            LIFO = False # Last In First OUT - remove newest messages if too much tokens
            token_counter_setup = TokenCounter(model_name, max_tokens_per_message_setup, LIFO)
            setup_messages = token_counter_setup.limit_tokens(Message.to_dict(setup_messages))
            setup_messages = Message.to_objects(setup_messages)
            
            # limit user messages by max token count
            FIFO = True # Last In First OUT - remove oldest messages if too much tokens
            token_counter_user = TokenCounter(model_name, max_tokens_per_message_user, FIFO)
            user_messages = token_counter_user.limit_tokens(Message.to_dict(user_messages))
            user_messages = Message.to_objects(user_messages)

            # combine all messages
            chat_messages = setup_messages + user_messages

            # call OpenAI chat completion API
            client = OpenAI()
            completion = client.chat.completions.create( \
                model=model_name,  messages=Message.serialize_messages(chat_messages))

            # assitant response
            assistant_response = completion.choices[0].message.content
            print(f"\nAssitant response: {assistant_response}")

            # save user message and assitant response
            assistant_message = Message(role="assistant", content=assistant_response)
            user_messages.append(assistant_message)
            Message.save_to_json(user_messages, user_chat_file, data_directory)
            #------------------------------------------------------------------------------------------------