from collections import defaultdict


def part12():
    partial_sums = defaultdict(lambda: 0)
    for x in range(300):
        for y in range(300):
            partial_sums[(x, y)] = (((((((x + 1) + 10) * (y + 1)) + 3031) * ((x + 1) + 10)) // 100 % 10) - 5 + partial_sums[x, y-1] + partial_sums[x-1, y] - partial_sums[x-1, y-1])
    cells = {(x - size + 2, y - size + 2, size):  partial_sums[(x, y)] + partial_sums[(x - size, y - size)] - partial_sums[(x - size, y)] - partial_sums[(x, y - size)] for size in range(2, 300) for y in range(size - 1, 300) for x in range(size - 1, 300)}
    return ','.join(map(str, max((x for x in cells if x[2] == 3), key=lambda x: cells[x])[:2])), ','.join(map(str, max(cells, key=lambda x: cells[x])))


def main():
    print(*part12())


if __name__ == '__main__':
    main()