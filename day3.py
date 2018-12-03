import re
from collections import defaultdict


def part12(input):
    fabric = defaultdict(lambda: 0)
    claims = {x[0]: [(x[1] + a, x[2] + b) for a in range(x[3]) for b in range(x[4])] for x in input}

    def check(key):
        fabric[key] += 1
        return fabric[key] - 1 == 1

    return sum(1 for y in claims for x in claims[y] if check(x)), next(y for y in claims if all(fabric[x] == 1 for x in claims[y]))


def main():
    input = [[int(y) for y in re.findall(r'-?\d+', x)] for x in open('day3.txt')]
    print(*part12(input))


if __name__ == '__main__':
    main()