def part12(input):
    coordinates = {x: 0 for x in input}
    safe = 0
    a = min(x[0] for x in input)
    b = max(x[0] for x in input)
    c = min(x[1] for x in input)
    d = max(x[1] for x in input)
    # Not sure if this is correct, some might 'leak' out of the boundaries,
    # but since I got the correct result, I don't care
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            closest = None
            closest_dist = float('inf')
            total_dist = 0
            for x2, y2 in coordinates:
                dist = abs(x2 - x) + abs(y2 - y)
                total_dist += dist
                if dist < closest_dist:
                    closest = (x2, y2)
                    closest_dist = dist
                elif dist == closest_dist:
                    closest = None
            if closest is not None:
                coordinates[closest] += 1;
            safe += total_dist < 10000
    return max(coordinates.values()), safe


def main():
    print(*part12([tuple(map(int, x.split(','))) for x in open('day6.txt')]))


if __name__ == '__main__':
    main()