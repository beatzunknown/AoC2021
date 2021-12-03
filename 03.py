with open('03.txt', 'r') as f:
    data = [[int(x) for x in l.rstrip()] for l in f.readlines()]

gamma = ''
epsilon = ''

for j in range(len(data[0])):
    most = sum(data[i][j] for i in range(len(data))) > (len(data)//2)
    gamma += chr(ord('0') + int(most))
    epsilon += chr(ord('0') + int(not most))

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

def solve_2(data, want_most):
    d = [[x for x in y] for y in data]
    for j in range(len(data[0])):
        if len(d) == 1:
            break
        most = sum(d[i][j] for i in range(len(d))) >= (len(d)/2)
        if want_most:
            new_d = [row for row in d if row[j] == int(most)]
        else:
            new_d = [row for row in d if row[j] == int(not most)]
        d = new_d
    return int(''.join(list(map(str, d[0]))), 2)

oxygen = solve_2(data, True)
scrubber = solve_2(data, False)

print('Part 1:', gamma * epsilon)
print('Part 2:', oxygen * scrubber)
