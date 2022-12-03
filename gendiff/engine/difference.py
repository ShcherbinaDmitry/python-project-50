def difference(dict1, dict2):
    diff = []
    new_dict = {**dict1, **dict2}
    sorted_keys = sorted(new_dict.keys())

    for key in sorted_keys:
        if key not in dict1:
            diff.append({
                'key': key,
                'operation': 'add',
                'new': dict2[key]
            })
        elif key not in dict2:
            diff.append({
                'key': key,
                'operation': 'removed',
                'old': dict1[key]
            })
        elif isinstance(dict1[key], dict) and isinstance(
                dict2[key], dict):
            child = difference(dict1[key], dict2[key])
            diff.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif dict1[key] == dict2[key]:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': dict1[key]
            })
        elif dict1[key] != dict2[key]:
            diff.append({
                'key': key,
                'operation': 'changed',
                'old': dict1[key],
                'new': dict2[key]
            })

    return diff

