board = [*'-' * 9]
check = ['012', '345', '678', '036', '147', '258', '048', '246']


def draw_board():
    for i in range(0, 7, 3):
        print([board[i], board[i + 1], board[i + 2]])


def is_game_over(board):
    for code in check:
        [a, b, c] = [*code]
        winner = board[int(a)] + board[int(b)] + board[int(c)]
        if winner in ['XXX', 'OOO']:
            return winner[0]
    if '-' not in board:
        return 'tie'
    return False


def make_best_move():
    best_score = 2
    best_move = None
    for i in range(9):
        if board[i] == '-':
            board[i] = 'O'
            score = minimax(True, board)
            board[i] = '-'
            if score < best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'


def minimax(x_turn, position):
    game_over = is_game_over(position)
    if game_over:
        return 0 if game_over == 'tie' else 1 if game_over == 'X' else -1

    scores = []
    for i in range(9):
        if position[i] == '-':
            position[i] = 'X' if x_turn else 'O'
            scores.append(minimax(not x_turn, position))
            position[i] = '-'
    return max(scores) if x_turn else min(scores)


while True:
    draw_board()
    coord = input('Enter position: ')
    if int(coord) in range(1, 10) and not board[int(coord) - 1] in ['X', 'O']:
        board[int(coord) - 1] = 'X'
        make_best_move()
    else:
        print('Wrong position.')

    game_over = is_game_over(board)
    if game_over:
        draw_board()
        print("It's a tie!" if game_over == 'tie' else game_over + ' won!')
        break
