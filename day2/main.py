import sys


def main():
    input_file = open("input", "r")
    lines = [line.strip() for line in input_file.readlines()]
    print(sum([score_part1(line) for line in lines]))
    print(sum([score_part2(line) for line in lines]))
    input_file.close()


def score_part1(line):
    if line == "B X":
        return 1
    if line == "C Y":
        return 2
    if line == "A Z":
        return 3
    if line == "A X":
        return 4
    if line == "B Y":
        return 5
    if line == "C Z":
        return 6
    if line == "C X":
        return 7
    if line == "A Y":
        return 8
    if line == "B Z":
        return 9


def score_part2(line):
    if line == "A X":
        return 3
    if line == "B X":
        return 1
    if line == "C X":
        return 2
    if line == "A Y":
        return 4
    if line == "B Y":
        return 5
    if line == "C Y":
        return 6
    if line == "A Z":
        return 8
    if line == "B Z":
        return 9
    if line == "C Z":
        return 7


if __name__ == "__main__":
    sys.exit(main())
