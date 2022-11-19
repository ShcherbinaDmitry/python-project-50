from gendiff.engine.generate_diff import generate_diff
import json


def test_plain_json_comparison():
  assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == open('./tests/fixtures/result.txt', 'r').read()