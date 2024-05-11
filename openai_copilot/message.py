import os
import json

'''
# Example usage:
file_path = "messages.json"
directory_path = "/path/to/directory"

messages = Message.load_from_json(file_path, directory=directory_path)
Message.save_to_json(messages, file_path, directory=directory_path)
'''

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content
    
    def serialize(self):
        return {"role": self.role, "content": self.content}
    
    @classmethod
    def deserialize(cls, data):
        return cls(data["role"], data["content"])

    @staticmethod
    def load_from_json(file_path, directory=None):
        if directory:
            file_path = os.path.join(directory, file_path)
        with open(file_path, "r") as file:
            data = json.load(file)
        
        if data: return Message.deserialize_messages(data)
        else: return None

    @staticmethod
    def save_to_json(messages, file_path, directory=None):
        if directory:
            file_path = os.path.join(directory, file_path)
        data = Message.serialize_messages(messages)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def serialize_messages(messages):
        return [message.serialize() for message in messages]

    @staticmethod
    def deserialize_messages(json_data):
        return [Message(**message) for message in json_data]  