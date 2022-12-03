DEFAULT_INDENT = 4


def to_str(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + DEFAULT_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nested_value}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def make_line(dictionary, key, depth, sign):
    return f'{" " * depth}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], depth + DEFAULT_INDENT)}'


def format_stylish(diff, depth=0):
    result = ['{']
    for dictionary in diff:
        op = dictionary['operation']
        if op == 'same':
            result.append(make_line(
                dictionary, 'value',
                depth, sign='    '
            ))

        if op == 'add':
            result.append(make_line(
                dictionary, 'new',
                depth, sign='  + '
            ))

        if op == 'removed' or op == 'changed':
            result.append(make_line(
                dictionary, 'old',
                depth, sign='  - '
            ))

        if op == 'changed':
            result.append(make_line(
                dictionary, 'new',
                depth, sign='  + '
            ))

        if dictionary['operation'] == 'nested':
            new_value = format_stylish(
                dictionary['value'],
                depth + DEFAULT_INDENT)
            result.append(
                f'{" " * depth}    {dictionary["key"]}: {new_value}')

    result.append(f'{" " * depth}}}')
    result = "\n".join(result)

    return result
