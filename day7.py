from collections import defaultdict
from itertools import count


def part1(followers, prerequisites, available):
    # using a dict because dicts are ordered by default
    done = {}
    while available:
        next = min(x for x in available if all(y in done for y in prerequisites[x]))
        done[next] = None
        available |= followers[next]
        available.remove(next)
    return ''.join(done)


def part2(followers, prerequisites, available):
    done = set()
    workers = [[0, None], [0, None], [0, None], [0, None], [0, None]]
    for cnt in count():
        for worker in sorted(workers, key=lambda x: x[0])[::-1]:
            worker[0] -= worker[0] > 0
            if not worker[0]:
                if worker[1] is not None:
                    done.add(worker[1])
                    available |= followers[worker[1]]
                try:
                    next = min(x for x in available if all(y in done for y in prerequisites[x]))
                    available.remove(next)
                    worker[:] = [ord(next) - 4, next]
                except ValueError:
                    worker[:] = [0, None]
        if all(not x[0] for x in workers):
            break
    return cnt


def main():
    input = [(x[5], x.strip()[-12]) for x in open('day7.txt')]
    followers = defaultdict(lambda: set())
    prerequisites = defaultdict(lambda: set())
    for x, y in input:
        prerequisites[y].add(x)
        followers[x].add(y)
    available = followers.keys() - prerequisites.keys()
    # send a copy of available to part1 because we are modifying it
    print(part1(followers, prerequisites, set(available)), part2(followers, prerequisites, available))


if __name__ == '__main__':
    main()