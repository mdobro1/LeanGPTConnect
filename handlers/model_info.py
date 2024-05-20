'''
# Example usage
reader = ModelInfoReader('model_info.json')
print("Description of gpt-4-turbo:", reader.get_model_description('gpt-4-turbo'))
print("Context window of gpt-4-turbo:", reader.get_context_window('gpt-4-turbo'))
print("Training data of gpt-4-turbo:", reader.get_training_data('gpt-4-turbo'))
print("Token count of gpt-4-turbo:", reader.get_token_count('gpt-4-turbo'))
'''

import json

#====================================
class ModelInfoHandler:
#====================================
    #------------------------------------------------------------------------------------------------
    def __init__(self, json_file):
    #------------------------------------------------------------------------------------------------
        self.json_file = json_file
        self.model_info = self.read_model_info()

    #------------------------------------------------------------------------------------------------
    def read_model_info(self):
    #------------------------------------------------------------------------------------------------
        with open(self.json_file, 'r', encoding='latin-1') as file:
            data = json.load(file)
            return data
        
    #------------------------------------------------------------------------------------------------
    def save_model_info(self, model_info):
    #------------------------------------------------------------------------------------------------
        with open(self.json_file, 'w', encoding='latin-1') as file:
            json.dump(model_info, file, indent=4)        

    #------------------------------------------------------------------------------------------------
    def get_model_description(self, model_name):
    #------------------------------------------------------------------------------------------------
        for model in self.model_info:
            if model['model'] == model_name:
                return model['description']
            
        return None

    #------------------------------------------------------------------------------------------------
    def get_context_window(self, model_name):
    #------------------------------------------------------------------------------------------------
        for model in self.model_info:
            if model['model'] == model_name:
                return model['context_window']
            
        return None

    #------------------------------------------------------------------------------------------------
    def get_training_data(self, model_name):
    #------------------------------------------------------------------------------------------------
        for model in self.model_info:
            if model['model'] == model_name:
                return model['training_data']
            
        return None

    #------------------------------------------------------------------------------------------------
    def get_token_count(self, model_name):
    #------------------------------------------------------------------------------------------------
        for model in self.model_info:
            if model['model'] == model_name:
                return model['token_count']
            
        return None