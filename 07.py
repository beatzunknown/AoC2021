import math

with open('07.txt', 'r') as f:
    positions = list(map(int, f.readline().rstrip().split(',')))

part_1_fuel = 9999999999999
for pos in range(max(positions)+1):
	fuel = sum([abs(pos-p) for p in positions])
	if fuel < part_1_fuel:
		part_1_fuel = fuel
		max_pos = pos

triangles = [0]
for i in range(1, max(positions)+1):
	triangles.append(triangles[i-1] + i)

def triangle(n):
	return triangles[n]

part_2_fuel = 9999999999999
for pos in range(max(positions)+1):
	fuel = sum([triangle(abs(pos-p)) for p in positions])
	if fuel < part_2_fuel:
		part_2_fuel = fuel
		max_pos = pos

print('Part 1:', part_1_fuel)
print('Part 2:', part_2_fuel)
