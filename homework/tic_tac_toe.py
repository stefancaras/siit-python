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


def make_best_move(for_x):
    scores = []
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X' if for_x else 'O'
            scores.append(minimax(not for_x, board, -2, 2))
            board[i] = '-'
        else:
            scores.append(-2 if for_x else 2)
    best_move = scores.index(max(scores) if for_x else min(scores))
    board[best_move] = 'X' if for_x else 'O'


def minimax(x_turn, position, alpha, beta):
    game_over = is_game_over(position)
    if game_over:
        return 0 if game_over == 'tie' else 1 if game_over == 'X' else -1

    scores = []
    for i in range(9):
        if position[i] == '-':
            position[i] = 'X' if x_turn else 'O'
            scores.append(minimax(not x_turn, position, alpha, beta))
            position[i] = '-'
            # alpha-beta pruning (increases speed)
            if x_turn:
                alpha = max(alpha, scores[-1])
            else:
                beta = min(beta, scores[-1])
            if beta <= alpha:
                break
    return max(scores) if x_turn else min(scores)


def play(player_x):
    draw_board()
    coord = input('Enter position (1-9): ')
    if coord.isnumeric() and int(coord) in range(1, 10) and board[int(coord) - 1] == '-':
        board[int(coord) - 1] = 'X' if player_x else 'O'
        if not is_game_over(board):
            make_best_move(not player_x)
    else:
        print('Not a valid number.')


is_x = True if input('Choose X or O: ').upper() == 'X' else False
if not is_x:
    board[0] = 'X'

while True:
    game_over = is_game_over(board)
    if game_over:
        draw_board()
        print("It's a tie!" if game_over == 'tie' else game_over + ' won!')
        break
    elif is_x:
        play('X')
    else:
        play(0)
