import re
from itertools import count


def part12(input):
    old_area = float('inf')
    for cnt in count():
        a = max(x + cnt * dx for x, y, dx, dy in input)
        b = min(x + cnt * dx for x, y, dx, dy in input)
        c = max(y + cnt * dy for x, y, dx, dy in input)
        d = min(y + cnt * dy for x, y, dx, dy in input)
        area = (a - b) * (c - d)
        if area > old_area:
            break
        old_area = area
    time = cnt - 1
    points = {(-b + x + time * dx, -d + y + time * dy) for x, y, dx, dy in input}
    drawing = [('#' if (x, y) in points else ' ' for x in range(a - b)) for y in range(c - d)]
    return '\n'.join(''.join(m) for m in (('#' if (x, y) in points else ' ' for x in range(a - b)) for y in range(c - d))), time


def main():
    input = [[int(y) for y in re.findall(r'-?\d+', x)] for x in open('day10.txt')]
    print(*part12(input))


if __name__ == '__main__':
    main()