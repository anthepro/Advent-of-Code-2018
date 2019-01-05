from collections import deque
from itertools import count


def manhattan_dist(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


def get_neighbours(x, y):
    return ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y))


def find_move(free_spots, start, goal, min_len):
    queue = deque([[start]])
    paths = set()
    min_path = float('inf')
    while queue:
        path = queue.popleft()
        if len(path) > min_len[0]:
            return
        if len(path) > min_path:
            min_len[0] = len(path)
            return min(paths)
        if path[-1] == goal:
            min_path = len(path)
            paths.add(tuple(path))
        for pos in get_neighbours(*path[-1]):
            if pos in free_spots:
                queue.append(path + [pos])
                free_spots.remove(pos)
    return None if not paths else min(paths)


def part12(goblins, elves, available_spots, elves_attack=3):
    for cnt in count():
        for unit in sorted(goblins.keys() | elves.keys()):
            free_spots = available_spots - (goblins.keys() | elves.keys())
            targets, units = (goblins, elves) if unit in elves else (elves, goblins)
            if not targets:
                return cnt * sum(elves.values() if elves else goblins.values())
            if unit not in units:
                continue
            if not any(x in targets for x in get_neighbours(*unit)):
                in_range_spots = {x for y in targets for x in get_neighbours(*y) if x in free_spots}
                if not in_range_spots:
                    continue
                min_len = [float('inf')]
                try:
                    new_unit = min((x for x in (find_move(set(free_spots), unit, a, min_len) for a in sorted(in_range_spots, key=lambda x: manhattan_dist(unit, x)) if manhattan_dist(unit, a) <= min_len[0]) if x is not None), key=lambda x: (len(x), x[-1], x[1]))[1]
                    units[new_unit] = units[unit]
                    del units[unit]
                    unit = new_unit
                except ValueError as e:
                    continue
            try:
                target = min((x for x in get_neighbours(*unit) if x in targets), key=lambda x: targets[x])
            except ValueError:
                continue
            targets[target] -= 3 if targets is elves else elves_attack
            if targets[target] <= 0:
                if targets is elves and elves_attack > 3:
                    return
                del targets[target]


def main():
    input = open('day15.txt').readlines()
    goblins = {(idx1, idx2): 200 for idx1, x in enumerate(input) for idx2, y in enumerate(x) if y == 'G'}
    elves = {(idx1, idx2): 200 for idx1, x in enumerate(input) for idx2, y in enumerate(x) if y == 'E'}
    available_spots = {(idx1, idx2) for idx1, x in enumerate(input) for idx2, y in enumerate(x) if y in {'.', 'G', 'E'}}
    print(part12(dict(goblins), dict(elves), set(available_spots)), next(x for x in (part12(dict(goblins), dict(elves), set(available_spots), y) for y in count(4)) if x is not None))


if __name__ == '__main__':
    main()