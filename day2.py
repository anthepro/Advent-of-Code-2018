# Who needs more code
from functools import reduce


def part1(input):
    return reduce(lambda x, y: x * y, (sum(any(x.count(c) == y for c in x) for x in input) for y in (2, 3)))


def part2(input):
    # sum(1 for ... if cond) rather than sum(cond for ...) because it's much faster in this case
    return next(''.join(c for c, d in zip(x, y) if c == d) for y in input for x in input if sum(1 for a, b in zip(x, y) if a != b) == 1)


def main():
    input = open('day2.txt').readlines()
    print(part1(input), part2(input))


if __name__ == '__main__':
    main()
