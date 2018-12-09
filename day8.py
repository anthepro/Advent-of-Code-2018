from collections import defaultdict


def part12(input):
    total_metadata = 0
    tree = defaultdict(lambda: [])
    while input:
        x = next(pos for pos, x in enumerate((x[0] for x in input)) if not x)
        metadata = input[x+1][0]
        metadata_vals = [input[x+y][0] for y in range(2, metadata + 2)]
        metadata_sum = sum(metadata_vals)
        total_metadata += metadata_sum
        node = metadata_sum if not tree[input[x][1]] else sum (tree[input[x][1]][y-1] for y in metadata_vals if 0 < y <= len(tree[input[x][1]]))
        tree[input[x-2][1]].append(node)
        input[x-2][0] -= x > 0
        input[x:x+metadata+2] = []
    return total_metadata, node


def main():
    print(*part12([[int(x), object()] for pos, x in enumerate(open('day8.txt').read().split())]))


if __name__ == '__main__':
    main()