def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def format_plain(diff, path=""):
    result = []
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"
        op = dictionary['operation']

        if op == 'add':
            result.append(
                f"Property '{property}' "
                f"was added with value: "
                f"{to_str(dictionary['new'])}"
            )

        if op == 'removed':
            result.append(f"Property '{property}' was removed")

        if op == 'nested':
            new_value = format_plain(dictionary['value'], f"{property}.")
            result.append(f"{new_value}")

        if op == 'changed':
            result.append(
                f"Property '{property}' was updated. "
                f"From {to_str(dictionary['old'])} to "
                f"{to_str(dictionary['new'])}")

    result = '\n'.join(result)

    return result
