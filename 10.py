with open('10.txt', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

SYNTAX_SCORES = {')':3, ']':57, '}':1197, '>':25137}
COMPLETE_SCORES = {')':1, ']':2, '}':3, '>':4}
MATCH = {'(':')', ')':'(',
		 '[':']', ']':'[',
		 '{':'}', '}':'{',
		 '<':'>', '>':'<'}

syntax_score = 0
complete_scores = []
for line in lines:
	stack = []
	error = False
	for c in line:
		if c in '([{<':
			stack.append(MATCH[c])
		elif c in ')]}>':
			if c != stack.pop():
				syntax_score += SYNTAX_SCORES[c]
				error = True
				break
	if not error:
		score = 0
		[score := 5*score + COMPLETE_SCORES[c] for c in stack[::-1]]
		complete_scores.append(score)

print('Part 1:', syntax_score)
print('Part 2:', sorted(complete_scores)[len(complete_scores)//2])
