import sys


def read_in():
    return [x.strip().split() for x in sys.stdin.readlines()]


def main():
    lines = read_in()
    print(lines)


if __name__ == '__main__':
    main()