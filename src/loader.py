import json
from .json_validator import Prompts

def prompts_loader(path):
    with open(path, "r") as file:
        data = json.load(file)
    return [Prompts(**item) for item in data]

