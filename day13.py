def part12(tracks, carts):
    turns = {'v': {'+': lambda turn: (('>', 'v', '<')[turn], (turn + 1) % 3), '/': lambda turn: ('<', turn), '\\': lambda turn: ('>', turn)},
             '<': {'+': lambda turn: (('v', '<', '^')[turn], (turn + 1) % 3), '/': lambda turn: ('v', turn), '\\': lambda turn: ('^', turn)},
             '^': {'+': lambda turn: (('<', '^', '>')[turn], (turn + 1) % 3), '/': lambda turn: ('>', turn), '\\': lambda turn: ('<', turn)},
             '>': {'+': lambda turn: (('^', '>', 'v')[turn], (turn + 1) % 3), '/': lambda turn: ('^', turn), '\\': lambda turn: ('v', turn)}}

    directions = {'^': lambda x, y: (x, y - 1), 'v': lambda x, y: (x, y + 1),
                  '>': lambda x, y: (x + 1, y), '<': lambda x, y: (x - 1, y)}
    part1 = None
    while True:
        new_carts = {}
        for cart in sorted(carts):
            direction, turn = carts[cart]
            cart = directions[direction](*cart)
            if cart in new_carts:
                del new_carts[cart]
                if part1 is None:
                    part1 = cart
            else:
                new_carts[cart] = turns[direction][tracks[cart]](turn) if tracks[cart] in turns[direction] else (direction, turn)
        if len(new_carts) == 1:
            return ','.join(map(str, part1)), ','.join(map(str, next(iter(new_carts))))
        carts = new_carts


def main():
    tracks = {(int(x), int(y)): symbol for y, row in enumerate(open('day13.txt').readlines()) for x, symbol in enumerate(row[:-1]) if symbol != ' '}
    carts = {x: (tracks[x], 0) for x in tracks if tracks[x] in {'^', '<', '>', 'v'}}
    for x in carts:
        tracks[x] = '|' if tracks[x] in {'^', 'v'} else '-'
    print(*part12(tracks, carts))


if __name__ == '__main__':
    main()