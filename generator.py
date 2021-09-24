import hashlib

# def get_hex(path):
#     with open(path, encoding='windows-1251') as f:
#         lines = f.readlines()
#         countries_json = json.dumps(lines)
#         for line in countries_json:
#             print(hashlib.md5(line.encode()).hexdigest())


def get_hex(path):
    with open(path, encoding='windows-1251') as f:
        next_line = next(f)
        for line in f:
            yield hashlib.md5(line.encode()).hexdigest()
            line = next_line


if __name__ == '__main__':
    for item in get_hex('countries.json'):
        print(item)
