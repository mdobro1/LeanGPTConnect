
from handlers.arguments_parser import ArgumentsParser
from handlers.copilot_handler import CopilotHandler    

#----------------------------------------------------
if __name__ == "__main__":
#----------------------------------------------------
    # parse arguments
    args = ArgumentsParser().parse_args()

    # run copilot
    CopilotHandler(args).run()