from collections import deque


def part12(players, last_marble):
    marbles = deque([0])
    scores = [0] * players
    for marble in range(1, last_marble + 1):
        if not marble % 23:
            marbles.rotate(-7)
            scores[marble%players] += marble + marbles.popleft()
            marbles.rotate(1)
        else:
            marbles.rotate(1)
            marbles.appendleft(marble)
    return max(scores)


def main():
    print(part12(470, 72170), part12(470, 72170 * 100))


if __name__ == '__main__':
    main()