import sys


def main():
    input_file = open("input", "r")
    lines = input_file.readlines()

    # Part 1
    total = 0
    for line in lines:
        line = line.strip()
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]

        chars_in_first = {}
        chars_in_both = {}
        for char in left:
            chars_in_first[char] = True
        for char in right:
            if char in chars_in_first:
                chars_in_both[char] = True

        for key in chars_in_both.keys():
            total += priority(key)
    print(total)

    # Part 2
    total = 0
    for i in range(0, len(lines), 3):
        j = i + 1
        k = j + 1
        chars_in_first = {}
        chars_in_first_and_second = {}
        chars_in_all = {}
        for char in lines[i]:
            chars_in_first[char] = True
        for char in lines[j]:
            if char in chars_in_first:
                chars_in_first_and_second[char] = True
        for char in lines[k]:
            if char in chars_in_first_and_second:
                chars_in_all[char] = True

        for key in chars_in_all.keys():
            total += priority(key)

    print(total)

    input_file.close()


def priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    elif ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
