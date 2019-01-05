import re
from functools import reduce
from math import sqrt
from day16 import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr


def part1(pointer, instructions):
    registers = [0, 0, 0, 0, 0, 0]
    while registers[pointer] < len(instructions):
        eval(instructions[registers[pointer]])
        registers[pointer] += 1
    return registers[0] - (not pointer)


# part2 is just the sum of all factors of a number in register 3 (in my case 10551288)
def part2():
    return sum(reduce(list.__add__, ([x, 10551288 // x] for x in range(1, int(sqrt(10551288))+1, 2 if 10551288 % 2 else 1) if not 10551288 % x)))


def main():
    pointer, *instructions = [x.strip() for x in open('day19.txt')]
    instructions = ['%s%s' % (x.replace(' ', '(', 1).replace(' ', ',', 2) , ',registers)') for x in instructions]
    print(part1(int(pointer[-1]), instructions), part2())


if __name__ == '__main__':
    main()