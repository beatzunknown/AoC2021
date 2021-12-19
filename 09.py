import numpy as np
import math
from cv2 import cv2

grid = [[int(x) for x in l.rstrip()] for l in open('09.txt', 'r').readlines()]

def is_local_min(r, c, grid):
	val = grid[r][c]
	for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
		if (0 <= r+dr < len(grid)) and (0 <= c+dc < len(grid[0])):
			if grid[r][c] >= grid[r+dr][c+dc]:
				return False
	return True

risk_lvl = 0
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if is_local_min(r, c, grid):
			risk_lvl += grid[r][c] + 1

# part 2 is connected components problem
grid = np.array(grid, dtype='uint8')
_, grid_binary = cv2.threshold(grid, 8, 255, cv2.THRESH_BINARY_INV)
n, _, stats, _ = cv2.connectedComponentsWithStats(grid_binary, connectivity=4)

basin_sizes = sorted([stats[i, cv2.CC_STAT_AREA] for i in range(1, n)], reverse=True)[:3]

print('Part 1:', risk_lvl)
print('Part 2:', math.prod(basin_sizes))
