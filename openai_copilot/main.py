import os
import json
import sys
from datetime import datetime
from message import Message
from openai import OpenAI

#---------------------------------------------
def main(prompt=None, message_context=None, model_name="gpt-3.5-turbo"):
#---------------------------------------------
    # init
    chat_messages = []
    if not prompt: prompt = input("Enter your prompt: ")
    user_message = Message(role="user", content=prompt)
    
    # get data dir
    data_directory = None
    if message_context: 
        data_directory = os.path.join("data", message_context)    
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

    # get chat file path
    file_name = f"user_chat.json"
    if data_directory: file_path = os.path.join(data_directory, file_name)
    else: file_path = file_name

    if not os.path.exists(file_path):
        # create chat file if not exists with very first user message
        chat_messages.append(user_message)
        Message.save_to_json(chat_messages, file_name, data_directory)
    else:
        # load existing messages and add user message
        chat_messages = Message.load_from_json(file_name, data_directory) 
        if chat_messages: chat_messages.append(user_message)

    # call OpenAI chat completion API
    client = OpenAI()
    completion = client.chat.completions.create( \
        model=model_name,  messages=Message.serialize_messages(chat_messages))

    # assitant response
    assistant_response = completion.choices[0].message.content
    print(f"\nAssitant response: {assistant_response}")

    # save user message and assitant response
    assistant_message = Message(role="assistant", content=assistant_response)
    chat_messages.append(assistant_message)
    Message.save_to_json(chat_messages, file_name, data_directory)
    

#----------------------------------------------------
if __name__ == "__main__":
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
