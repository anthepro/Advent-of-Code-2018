import re
from collections import defaultdict


def part12(input):
    time = defaultdict(lambda: [0 for x in range(60)])
    state = [None, False, None]
    for x in input:
        if len(x) == 6:
            state[2] = x[-1]
        else:
            if state[1]:
                time[state[2]][state[0]:x[-1]] = [y + 1 for y in time[state[2]][state[0]:x[-1]]]
            state[:2] = x[-1], not state[1]
    guard = max(time,  key=lambda x: sum(time[x]))
    guard2 = max(time, key=lambda x: max(time[x]))
    return guard * time[guard].index(max(time[guard])), guard2 * time[guard2].index(max(time[guard2]))
        
  
def main():
    input = [[int(y) for y in re.findall(r'-?\d+', x)] for x in sorted(open('day4.txt'), key=lambda y: y[:19])]
    print(*part12(input))
    
    
if __name__ == '__main__':
    main()