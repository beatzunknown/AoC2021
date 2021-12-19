energy = [[int(x) for x in l.rstrip()] for l in open('11.txt', 'r').readlines()]

part_1 = flash_count = step = 0
flashed = []
while len(flashed) < 100:
    if step == 100:
        part_1 = flash_count
    flashed = []
    for r in range(len(energy)):
        for c in range(len(energy[r])):
            energy[r][c] += 1
    no_flash = False
    while not no_flash:
        no_flash = True
        for r in range(len(energy)):
            for c in range(len(energy[r])):
                if energy[r][c] > 9:
                    no_flash = False
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nc, nr = c+dc, r+dr
                            if (0 <= nr < len(energy)) and (0 <= nc < len(energy[0])):
                                if dr == dc == 0:
                                    energy[nr][nc] = -1000
                                    flashed.append((nr, nc))
                                else:
                                    energy[nr][nc] += 1
    flash_count += len(flashed)
    for r,c in flashed:
        energy[r][c] = 0
    step += 1

print('Part 1:', part_1)
print('Part 2:', step)
