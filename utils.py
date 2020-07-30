import json


def get_json_conf():
    with open('configs/logger.json', 'r') as f:
        config = json.load(f)
    return config

