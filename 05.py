lines = []
with open('05.txt', 'r') as f:
    for line in f.readlines():
        start, end = line.split(' -> ')
        line = start.split(',') + end.split(',')
        lines.append(list(map(int, line)))

part_1 = part_2 = 0

graph = [[0 for i in range(1000)] for j in range(1000)]
hori = list(filter(lambda x: x[1]==x[3], lines))
vert = list(filter(lambda x: x[0]==x[2], lines))
diag = list(filter(lambda x: abs(x[0]-x[2])==abs(x[1]-x[3]), lines))

for x1,y1,x2,y2 in hori:
    stepdir = (-1)**int(x1 > x2)
    for i in range(x1, x2 + stepdir, stepdir):
        graph[i][y1] += 1

for x1,y1,x2,y2 in vert:
    stepdir = (-1)**int(y1 > y2)
    for i in range(y1, y2 + stepdir, stepdir):
        graph[x1][i] += 1

part_1 = sum([len(list(filter(lambda x: x>1, line))) for line in graph])

for x1,y1,x2,y2 in diag:
    stepdir_x = (-1)**int(x1 > x2)
    stepdir_y = (-1)**int(y1 > y2)
    for i in range(abs(x1-x2)+1):
        graph[x1+i*stepdir_x][y1+i*stepdir_y] += 1

part_2 = sum([len(list(filter(lambda x: x>1, line))) for line in graph])

print('Part 1:', part_1)
print('Part 2:', part_2)
