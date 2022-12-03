from gendiff.engine.formatters.stylish import format_stylish
from gendiff.engine.formatters.plain import format_plain
from gendiff.engine.formatters.json import format_json


def get_formatter(formatter):
  if formatter == 'stylish':
    return format_stylish
  if formatter == 'plain':
    return format_plain
  if formatter == 'json':
    return format_json

  raise ValueError(f"Unknown formatter: {formatter}")
