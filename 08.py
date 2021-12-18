patterns = []
values = []
with open('08.txt', 'r') as f:
    for line in f.readlines():
    	p, v = line.split(' | ')
    	patterns.append(p.split())
    	values.append(v.split())

num_unique = sum(len(list(filter(lambda x: len(x) in [2,3,4,7], v))) for v in values)
known_lengths = {2: '1', 3: '7', 4: '4', 7: '8'}

total = 0
for i in range(len(patterns)):
	sets = {len(p):set(p) for p in patterns[i]}
	num = ""
	for v in values[i]:
		v = set(v)
		# handle 1,4,7,8
		if len(v) in known_lengths.keys():
			num += known_lengths[len(v)]
		# handle 2,3,5
		elif len(v) == 5:
			if len(v & sets[4]) == 2:
				num += '2'
			elif len(v & sets[2]) == 2:
				num += '3'
			else:
				num += '5'
		# handle 0,6,9
		elif len(v) == 6:
			if len(v & sets[4]) == 4:
				num += '9'
			elif len(v & sets[2]) == 2:
				num += '0'
			else:
				num += '6'
	total += int(num)

print('Part 1:', num_unique)
print('Part 2:', total)
