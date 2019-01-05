from collections import defaultdict
import re


def addr(a, b, c, registers):
    registers[c] = registers[a] + registers[b]
    return registers


def addi(a, b, c, registers):
    registers[c] = registers[a] + b
    return registers


def mulr(a, b, c, registers):
    registers[c] = registers[a] * registers[b]
    return registers


def muli(a, b, c, registers):
    registers[c] = registers[a] * b
    return registers


def banr(a, b, c, registers):
    registers[c] = registers[a] & registers[b]
    return registers


def bani(a, b, c, registers):
    registers[c] = registers[a] & b
    return registers


def borr(a, b, c, registers):
    registers[c] = registers[a] | registers[b]
    return registers


def bori(a, b, c, registers):
    registers[c] = registers[a] | b
    return registers


def setr(a, b, c, registers):
    registers[c] = registers[a]
    return registers


def seti(a, b, c, registers):
    registers[c] = a
    return registers


def gtir(a, b, c, registers):
    registers[c] = a > registers[b]
    return registers


def gtri(a, b, c, registers):
    registers[c] = registers[a] > b
    return registers


def gtrr(a, b, c, registers):
    registers[c] = registers[a] > registers[b]
    return registers


def eqir(a, b, c, registers):
    registers[c] = a == registers[b]
    return registers


def eqri(a, b, c, registers):
    registers[c] = registers[a] == b
    return registers


def eqrr(a, b, c, registers):
    registers[c] = registers[a] == registers[b]
    return registers


def part1(input):
    functions = {addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}
    cnt = 0
    opcodes = defaultdict(lambda: set(functions))
    for x in input:
        before = x[:4]
        op, *args = x[4:8]
        after = x[8:]
        possibles = {f for f in functions if f(*args, before[:]) == after}
        cnt += len(possibles) >= 3
        opcodes[op] &= possibles
    print(cnt)
    while not all(len(x) == 1 for x in opcodes.values()):
        decided = {next(iter(x)) for x in opcodes.values() if len(x) == 1}
        opcodes = {x: (y - decided if len(y) > 1 else y) for x, y in opcodes.items()}
    return opcodes


def part2(input, opcodes):
    registers = [0, 0, 0, 0]
    for op, *args in input:
        registers = next(iter(opcodes[op]))(*args, registers)
    return registers[0]


def main():
    input1, input2 = open('day16.txt').read().split('\n\n\n')
    opcodes = part1((list(map(int, re.findall(r'-?\d+', x))) for x in input1.split('\n\n')))
    print(part2((map(int, x.split()) for x in input2.strip().split('\n')), opcodes))


if __name__ == '__main__':
    main()