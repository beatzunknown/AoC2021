with open('01.txt') as f:
    data = list(map(int, [l.rstrip() for l in f.readlines()]))

def solve(data, window):
    return sum([sum(data[i-window:i]) > sum(data[i-1-window:i-1]) for i in range(window+1, len(data)+1)])

print('Part 1:', solve(data, 1))
print('Part 2:', solve(data, 3))
