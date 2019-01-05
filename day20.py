from collections import defaultdict


def part12(input):
    directions = {'E': lambda x, y: (x, y + 1), 'W': lambda x, y: (x, y - 1), 'N': lambda x, y: (x - 1, y),
                  'S': lambda x, y: (x + 1, y)}
    positions = []
    pos = last_pos = (0, 0)
    distances = defaultdict(lambda: float('inf'), {pos: 0})
    for x in input:
        if x == '(':
            positions.append(pos)
        elif x == ')':
            pos = positions.pop()
        elif x == '|':
            pos = positions[-1]
        else:
            pos = directions[x](*pos)
            distances[pos] = min(distances[pos], distances[last_pos] + 1)
        last_pos = pos
    return max(distances.values()), sum(1 for x in distances.values() if x >= 1000)


def main():
    print(*part12(open('day20.txt').read().strip()[1:-1]))


if __name__ == '__main__':
    main()
