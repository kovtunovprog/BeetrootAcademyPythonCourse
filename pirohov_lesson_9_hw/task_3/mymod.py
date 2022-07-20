def count_lines(name: str) -> int:
    f = open(name)
    print(f'Count of lines: {len(f.readlines())}')

def count_chars(name):
    f = open(name)
    print(f'Count of chars: {len(f.read())}')

def text(name):
    count_lines(name)
    count_chars(name)

def main():

    name = input('File name?\n')
    text(name)

if __name__ == '__main__':
    main()


