'''
# Example usage:
file_path = "prompts.json"
batch_prompt = BatchPrompt(file_path)

# Read prompts from file
prompts = batch_prompt.read_prompts()
print("prompts read from file:", prompts)

# Append new question
new_question = "How can I ensure scalability in my microservices architecture?"
prompts.append(new_question)

# Write prompts back to file
batch_prompt.write_prompts(prompts)
print("New question written to file:", new_question)
'''
import json

#====================================
class BatchPrompt:
#====================================
    #------------------------------------------------------------------------------------------------
    def __init__(self, file_path):
    #------------------------------------------------------------------------------------------------
        self.file_path = file_path

    #------------------------------------------------------------------------------------------------
    def read_prompts(self):
    #------------------------------------------------------------------------------------------------
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data.get("prompts", [])
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return []

    #------------------------------------------------------------------------------------------------
    def write_prompts(self, prompts):
    #------------------------------------------------------------------------------------------------
        data = {"prompts": prompts}
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)


