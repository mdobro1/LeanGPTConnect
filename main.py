import os
import json
import sys
from datetime import datetime
from utils.message import Message
from openai import OpenAI
from utils.batch_prompt import BatchPrompt
from utils.token_count import TokenCounter
from utils.model_info import ModelInfoReader

#---------------------------------------------
def main(prompt : str = None, message_context=None, model_name="gpt-3.5-turbo"):
#---------------------------------------------
    # init
    setup_messages = []
    user_messages = []
    user_prompts = []
    model_info : ModelInfoReader = ModelInfoReader("models/models_info.json")
    max_tokens = model_info.get_token_count(model_name)


    # append user prompt
    if not prompt or len(prompt.strip()) < 1: prompt = input("Enter your prompt: ")
    else:
        if not ".json" in prompt.lower() or not os.path.exists(prompt):
            if  not os.path.exists(prompt): print(f"Warning! Batch file {prompt} not found!")  
            # interactive prompt mode
            user_prompts.append(prompt)
        else:
            # batch prompt mode
            batch_prompt = BatchPrompt(prompt)
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
    

#----------------------------------------------------
if __name__ == "__main__":
#----------------------------------------------------
    # user prompt arg
    if len(sys.argv) == 2: main(sys.argv[1])
    else: 
        # user prompt & data context args
        if len(sys.argv) == 3: context_arg = main(sys.argv[1], sys.argv[2])
        else: 
            # user prompt, data context & model args
            if len(sys.argv) > 3: context_arg = main(sys.argv[1], sys.argv[2], sys.argv[3])
            else:
                # default params (interactive mode)
                main()
