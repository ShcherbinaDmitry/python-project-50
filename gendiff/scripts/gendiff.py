#!/usr/bin/env python3
import argparse
from gendiff.engine.generate_diff import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', nargs='?', help='set format of output', default='plain')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


# def generate_diff(file1, file2):
#     print('Finding difference')

#     return {
#         'result': 'success'
#     }


if __name__ == '__main__':
    main()