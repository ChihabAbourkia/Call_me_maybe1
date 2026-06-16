from .parser import argparser
from .loader import prompts_loader, function_loader
def main():
    print("🤖 Starting LLM fuction calling system....")
    parser = argparser()

    print("📂 Loading Functions and promts...")
    functions = function_loader(parser.functions_definition)
    if not functions:
        raise RuntimeError("No function difinetion found...")
    prompts = prompts_loader(parser.input)
    if not prompts:
        raise RuntimeError("No input prompts found. Please provide at least one prompt.")


if __name__ == "__main__":
    main()
