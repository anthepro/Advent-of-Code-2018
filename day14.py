# ugly brute force solution, but I am really not in a condition to think atm
def main():
    elves = [0, 1]
    scoreboard = [3, 7]
    while '894501' not in ''.join(map(str, scoreboard[-7:])):
        scoreboard.extend([int(x) for x in str(sum((scoreboard[y] for y in elves)))])
        elves = [(scoreboard[x] + x + 1) % len(scoreboard) for x in elves]
        if len(scoreboard) == 894511:
            print(''.join(map(str, scoreboard[894501:])))
    print(''.join(map(str, scoreboard)).find('894501'))


if __name__ == '__main__':
    main()