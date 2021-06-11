import yaml


def yaml_to_dict(filename: str) -> dict:
    with open(filename) as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)
            return {}