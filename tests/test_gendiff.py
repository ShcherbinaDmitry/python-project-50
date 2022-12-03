from gendiff.engine.generate_diff import generate_diff


def test_stylish_plain_diff():
    json_dict_1 = './tests/fixtures/plain/dict1.json'
    json_dict_2 = './tests/fixtures/plain/dict2.json'
    fixture = './tests/fixtures/plain/result.txt'

    # Testing for plain json
    assert generate_diff(json_dict_1, json_dict_2) == open(fixture, 'r').read()

    # Testing for yaml
    yaml_dict_1 = './tests/fixtures/plain/dict1.yml'
    yaml_dict_2 = './tests/fixtures/plain/dict2.yml'
    assert generate_diff(yaml_dict_1, yaml_dict_2) == open(fixture, 'r').read()


def test_stylish_nested_diff():
    json_dict_1 = './tests/fixtures/nested/dict1.json'
    json_dict_2 = './tests/fixtures/nested/dict2.json'
    fixture = './tests/fixtures/nested/stylish_result.txt'

    # Testing for plain json
    assert generate_diff(json_dict_1, json_dict_2) == open(fixture, 'r').read()

    # Testing for yaml
    yaml_dict_1 = './tests/fixtures/nested/dict1.yml'
    yaml_dict_2 = './tests/fixtures/nested/dict2.yml'
    assert generate_diff(yaml_dict_1, yaml_dict_2) == open(fixture, 'r').read()


def test_plain_nested_diff():
    dict_1 = './tests/fixtures/nested/dict1.json'
    dict_2 = './tests/fixtures/nested/dict2.json'
    fixture = './tests/fixtures/nested/plain_result.txt'

    assert generate_diff(dict_1, dict_2, 'plain') == open(fixture, 'r').read()


def test_json_nested_diff():
    dict_1 = './tests/fixtures/nested/dict1.json'
    dict_2 = './tests/fixtures/nested/dict2.json'
    fixture = './tests/fixtures/nested/json_result.txt'

    assert generate_diff(dict_1, dict_2, 'json') == open(fixture, 'r').read()
