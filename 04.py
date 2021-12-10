with open('04.txt', 'r') as f:
    choices, *data = f.readlines()
    choices = choices.split(',')

boards = []
for i in range(len(data)//6):
    boards.append([row.split() for row in data[i*6+1:i*6+6]])

def check(board):
    for i in range(len(board)):
        if not (any(board[i]) and any([board[j][i] for j in range(len(board))])):
            return True
    return False

def calc_score(board, choice):
    return sum(list(map(int, filter(None, sum(board, []))))) * int(choice)

won = set()
for choice in choices:
    for (x, board) in enumerate(boards):
        if x in won:
            continue
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == choice:
                    board[i][j] = ''
                    if check(board):
                        part_2 = calc_score(board, choice)
                        if not won:
                            part_1 = part_2
                        won.add(x)

print('Part 1:', part_1)
print('Part 2:', part_2)
