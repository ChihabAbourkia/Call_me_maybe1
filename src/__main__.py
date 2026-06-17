from .parser import argparser
from .loader import prompts_loader, function_loader
from .constrained_decoding import system_prompt_builder
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

    for f in functions:
        for p , t in f.parameters.items():
            print(f"{p} {t}\n")
    print("⚙️ Sytem prompt...")
    prompt_system = system_prompt_builder(functions)
    print(prompt_system)
    print("🛠️ Loading model...")
    model = Small_LLM_Model(parser.model)
    tokens = model.encode("hello")[0].tolist()
    logits = model.get_logits_from_input_ids(tokens)
    next = np.argmax(logits)
    print(f" \n {next}")
    ansswer = model.decode(next)
    print(ansswer)


if __name__ == "__main__":
    main()
