import tiktoken
import sys

#====================================
class TokenCounter:
#====================================
    #------------------------------------------------------------
    def __init__(self, model_name="gpt-3.5-turbo-0613", max_tokens_threshold : int = 1000, remove_first_item : bool = True):
    #------------------------------------------------------------
        self.model_name = model_name
        self.max_tokens_threshold = max_tokens_threshold
        self.remove_first_item = remove_first_item


    #------------------------------------------------------------
    def limit_tokens(self, messages):  
    #------------------------------------------------------------
        # init
        result = messages
        dict_messages = [dict(role=m.role, content=m.content) for m in messages]
        # get initial messages token count
        messages_token_count = TokenCounter.count_tokens(dict_messages, self.model_name)

        # go!
        while messages_token_count > self.max_tokens_threshold:
            # get messages token count
            messages_token_count = TokenCounter.count_tokens(dict_messages, self.model_name)

            if self.remove_first_item:
                messages.pop(0) # FIFO: remove first message
            else:
                messages.pop() # LIFO: remove last mennsage

            # recusively call this function until we're under the threshold
            result = self.limit_tokens(messages, self.max_tokens_threshold, self.remove_first_item, self.model_name)  
        
        # done!
        return result
    
    #-------------------------------------------------------------------------
    @staticmethod
    def count_tokens(messages, model_name="gpt-3.5-turbo-0613"):
    #
    # source: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    #-------------------------------------------------------------------------
        """Return the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model_name)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model_name in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
            }:
            tokens_per_message = 3
            tokens_per_name = 1
        elif model_name == "gpt-3.5-turbo-0301":
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif "gpt-3.5-turbo" in model_name:
            print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
            return TokenCounter.count_tokens(messages, model_name="gpt-3.5-turbo-0613")
        elif "gpt-4" in model_name:
            print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
            return TokenCounter.count_tokens(messages, model_name="gpt-4-0613")
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model_name}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
            )
        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens