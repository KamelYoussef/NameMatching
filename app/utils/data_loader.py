import yaml

def load_name_list():
    with open("app/names.yaml", "r") as file:
        return yaml.safe_load(file)
