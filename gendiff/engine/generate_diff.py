import json


def load_file(filepath):
    return json.load(open(filepath))


def join_dictionaries(dict1, dict2):
    return {**dict1, **dict2}


def generate_diff(filepath1, filepath2):
    dict1 = load_file(filepath1)
    dict2 = load_file(filepath2)

    result_dict = join_dictionaries(dict1, dict2)

    result = "{\n"

    for (key, value) in sorted(result_dict.items(), key=lambda d: d[0]):
        if (key not in dict1):
            result += f"  + {key}: {value}\n"
        elif (key not in dict2):
            result += f"  - {key}: {value}\n"
        elif (dict1[key] == dict2[key]):
            result += f"    {key}: {value}\n"
        else:
            result += f"  - {key}: {dict1[key]}\n"
            result += f"  + {key}: {dict2[key]}\n"

    result += "}"

    print(dict1)
    print(dict2)

    return result
