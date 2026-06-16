from .parser import argparser
from .loader import prompts_loader, function_loader
def main():
    print("🤖 Starting LLM fuction calling system....")
    parser = argparser()

    print("Loading pompts and functions difinetion")
    prompts = prompts_loader(parser.input)
    function  = function_loader(parser.functions_definition)
    

if __name__ == "__main__":
    main()
