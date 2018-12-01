from itertools import accumulate, cycle


def part1(input):
    return sum(int(x) for x in input)


def part2(input):
    seen = {0}
    return next(x for x in accumulate(cycle(map(int, input))) if x in seen or seen.add(x))


def main():
    input = open('day1.txt').readlines()
    print(part1(input), part2(input))


if __name__ == '__main__':
    main()