import json

def str_to_dict(dictionnaire : str) -> dict:
    return json.loads(dictionnaire)