def part1(input):
    x = 1
    while(x < len(input)):
        if input[x-1] == input[x].swapcase():
            del input[x-1:x+1]
            x -= 1 if x > 1 else 0
        else:
            x += 1
    return len(input)

def part2(input):
    return min(part1([y for y in input if y.casefold() != x]) for x in {z.casefold() for z in input})


def main():
    input = open('day5.txt').read()
    print(part1(list(input)), part2(input))

if __name__ == '__main__':
    main()