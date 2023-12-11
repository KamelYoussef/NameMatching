import yaml

def load_name_list():
    with open("data/names.yaml", "r") as file:
        return yaml.safe_load(file)
