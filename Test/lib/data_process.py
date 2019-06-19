# encoding=utf-8

import json

from lib.file_process import read_file


def to_json(content):
    # print(type(content))
    if isinstance(content, str):
        return json.loads(content)
    elif isinstance(content, bytes):
        content = content.decode('utf-8')
        # print('type after decode',type(content))
        return json.loads(content)
    else:
        print("don't support this type:", type(content))

if __name__ == '__main__':
    file = '/Users/yangcaihua/Documents/Dev/Test/personas/test_positive.json'
    rs = read_file(file)
    print(to_json(rs))