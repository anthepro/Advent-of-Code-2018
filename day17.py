import re


def part12():
    clay = set()
    for line in open('day17.txt'):
        vals = [int(x) for x in re.findall(r'-?\d+', line)]
        clay |= {(vals[0], y) for y in range(vals[1], 1 + vals[2])} if line[0] == 'x' else {(x, vals[0]) for x in range(vals[1], 1 + vals[2])}
    bottom = max(x[1] for x in clay)
    top = min(x[1] for x in clay)
    flowing = set()
    still = set()
    falling = {(500, 0)}
    spreading = set()
    while falling or spreading:
        while falling:
            pos = falling.pop()
            while pos[1] < bottom:
                new_pos = (pos[0], pos[1] + 1)
                if new_pos in clay:
                    spreading.add(pos)
                    break
                flowing.add(new_pos)
                pos = new_pos
        while spreading:
            pos = spreading.pop()
            tmp = set()
            sides = set()
            for x in range(-1, 2, 2):
                pos_ = pos
                while pos_ not in clay:
                    tmp.add(pos_)
                    new_pos = (pos_[0], pos_[1] + 1)
                    if new_pos not in clay and new_pos not in still:
                        sides.add(pos_)
                        break
                    pos_ = (pos_[0] + x, pos_[1])
            if sides:
                flowing |= tmp
                falling |= sides
            else:
                still |= tmp
                spreading.add((pos[0], pos[1] - 1))
    return sum(1 for x in (flowing | still) if x[1] >= top), sum(1 for xp in still if xp[1] >= top)


if __name__ == '__main__':
    print(*part12())
