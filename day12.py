from collections import defaultdict


def part12(state, transitions):
    last_totals = [0, 0, 0, 0, 0]
    for x in range(1, 5000000001):
        state = defaultdict(lambda: False, {x: transitions[''.join(('.', '#')[state[y]] for y in range(x - 2, x + 3))] == '#' for x in range(min(state) - 2, max(state) + 2)})
        total = sum(x for x in state if state[x])
        if x == 20:
            part1 = total
        last_totals.append(total)
        del last_totals[0]
        if len({last_totals[x+1] - last_totals[x] for x in range(len(last_totals) - 1)}) == 1:
            break
    return part1, total + (500000000 - x) * (last_totals[1] - last_totals[0])


def main():
    input = open('day12.txt').readlines()
    initial_state, transitions = defaultdict(lambda: False, {idx: x == '#' for idx, x in enumerate(input[0].split()[-1])}), dict(x.strip().split(' => ') for x in input[2:])
    print(*part12(initial_state, transitions))


if __name__ == '__main__':
    main()