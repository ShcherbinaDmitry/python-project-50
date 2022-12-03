import json
import yaml


def parse_json(filepath):
    return json.load(open(filepath))


def parse_yaml(filepath):
    return yaml.load(open(filepath), Loader=yaml.Loader)


def parse_file(filepath):
    if (filepath.endswith('.json')):
        return parse_json(filepath)
    elif (filepath.endswith('.yml') or filepath.endswith('yaml')):
        return parse_yaml(filepath)
    raise ValueError(f"Extension not supported: {filepath}")
