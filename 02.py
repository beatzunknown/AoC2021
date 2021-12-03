with open('02.txt', 'r') as f:
    data = [l.rstrip().split() for l in f.readlines()]

depth = pos = 0
for d, v in data:
    if d == 'forward':
        pos += int(v)
    elif d == 'down':
        depth += int(v)
    elif d == 'up':
        depth -= int(v)
part_1 = depth*pos

depth = pos = aim = 0
for d, v in data:
    if d == 'forward':
        pos += int(v)
        depth += aim * int(v)
    elif d == 'down':
        aim += int(v)
    elif d == 'up':
        aim -= int(v)
part_2 = depth*pos

print('Part 1:', part_1)
print('Part 2:', part_2)
