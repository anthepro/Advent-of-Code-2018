def calculate(x, y, input):
    adjacent = [input[a] for a in {(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x - 1, y + 1)} if a in input]
    if input[(x, y)] == '.':
        return '|' if sum(1 for x in adjacent if x == '|') > 2 else '.'
    if input[(x, y)] == '|':
        return '#' if sum(1 for x in adjacent if x == '#') > 2 else '|'
    if input[(x, y)] == '#':
        return '#' if '#' in adjacent and '|' in adjacent else '.'


def part12(input, time):
    seen = {}
    values = {}
    for min in range(time):
        input = {y: calculate(*y, input) for y in input}
        state = tuple((x, y) for x, y in input.items())
        values[min] = sum(1 for x in input.values() if x == '#') * sum(1 for x in input.values() if x == '|')
        if state in seen:
            break
        seen[state] = min
    else:
        return values[min]
    return values[seen[state]+(time-seen[state])%(min-seen[state])-1]


def main():
    input = {(idx1, idx2): y for idx1, x in enumerate(open('day18.txt')) for idx2, y in enumerate(x.strip())}
    print(part12(input, 10), part12(input, 1000000000))


if __name__ == '__main__':
    main()