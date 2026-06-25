from .parser import argparser
from .loader import prompts_loader, function_loader
from .constrained_decoding import system_prompt_builder, vocab_loader
from llm_sdk.llm_sdk import Small_LLM_Model
import numpy as np


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

    print("⚙️ Sytem prompt...")
    prompt_system = system_prompt_builder(functions)

    print("🛠️ Loading model...")
    try:
        model = Small_LLM_Model(parser.model)
    except OSError:
        raise RuntimeError(f"Model {parser.model} not found or field to download")
    print("✅ building valid ids")
    path = model.get_path_to_tokenizer_file()
    print(path)
    


if __name__ == "__main__":
    main()
