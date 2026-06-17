import json

def system_prompt_builder(functions):
    lines = [
        "STRICT SYSTEM RULES: use ONLY a matching function "
        "from the list below",
        "If No function matches the user's intent (even if "
        "types match), set name:\"none\".",
        "Never use an unrelated function for a differnet task.",
        "",
        "Available functions:",
    ]
    for f in functions:
        param = []
        for p, info in f.parameters.items():
            param.append(f"{p} : {info.type}")
            param_str = ",".join(param)
        lines.append(f"{f.name}({param_str}): {f.description}")
        lines.append('Output ONLY valid JSON: '
                 '{"name": "<fn>", "args": "{<args>}"}')
    return "\n".join(lines)

def vocab_loader(path):
    with open(path, "r") as file:
        data = json.load(file)
        vocab = data.get("model", {}).get("vocab", {})
        return vocab

def vocab_filter(vocab):
    

