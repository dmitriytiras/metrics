import re

if __name__ == '__main__':
    value = '$me!*)(A_'

    if re.search('^[a-zA-Z0-9_]+$', value) is None:
        print(re.sub('[a-zA-Z0-9_]', '', value))


