from gendiff.engine.parser import parse_file
from gendiff.engine.formatters import get_formatter
from gendiff.engine.difference import difference

def generate_diff(filepath1, filepath2, format = 'stylish'):
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    formatter = get_formatter(format)

    diff = difference(dict1, dict2)
    result = formatter(diff)

    return result

