def part12():
    seeny = set()
    seenx = set()
    part1 = part2 = None
    x = 15028787
    y = 65536
    while True:
        x = (x + (y & 255) & ((1 << 24) - 1)) * 65899 & ((1 << 24) - 1)
        if y >> 8:
            y >>= 8
            continue
        if not seenx:
            part1 = x
        if x not in seenx:
            part2 = x
        seenx.add(x)
        y = x | (1 << 16)
        if y in seeny:
            return part1, part2
        seeny.add(y)
        x = 15028787


if __name__ == '__main__':
    print(*part12())
