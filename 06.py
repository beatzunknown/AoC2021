with open('06.txt', 'r') as f:
    fishes = list(map(int, f.readline().rstrip().split(',')))
    timer_counts = {i:fishes.count(i) for i in range(9)}

for day in range(256):
    if day == 80:
        part_1 = sum(timer_counts.values())
    new = timer_counts[0]
    for i in range(8):
        timer_counts[i] = timer_counts[i+1]
    timer_counts[6] += new
    timer_counts[8] = new
part_2 = sum(timer_counts.values())

print('Part 1:', part_1)
print('Part 2:', part_2)
