import sys


def main():
    input_file = open("input", "r")
    calorie_counts = [sum([int(calories) for calories in elf.split('\n')]) for elf in
        input_file.read().strip().split('\n\n')]
    print(max(calorie_counts))

    calorie_counts.sort(reverse=True)
    print(sum(calorie_counts[0:3]))
    input_file.close()


if __name__ == "__main__":
    sys.exit(main())
