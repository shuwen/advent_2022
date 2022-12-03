import sys


def main():
    input_file = open("input", "r")
    lines = [line.strip() for line in input_file.readlines()]
    total = 0
    print(total)
    input_file.close()


if __name__ == "__main__":
    sys.exit(main())
