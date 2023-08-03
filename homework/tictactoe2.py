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
    best_score = -2 if for_x else 2
    best_move = 9
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X' if for_x else 'O'
            score = minimax(not for_x, board, -2, 2)
            board[i] = '-'
            if (score if for_x else best_score) > (best_score if for_x else score):
                best_score = score
                best_move = i
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


is_x = True if input('Choose X or O: ') == 'X' else False

while True:
    game_over = is_game_over(board)
    if game_over:
        print("It's a tie!" if game_over == 'tie' else game_over + ' won!')
        break
    draw_board()
    if is_x:
        coord = input('Enter position: ')
        if int(coord) in range(1, 10) and board[int(coord) - 1] == '-':
            board[int(coord) - 1] = 'X'
        else:
            print('Wrong position.')
            continue
        if not is_game_over(board):
            make_best_move(False)
    else:
        make_best_move(True)
        if not is_game_over(board):
            coord = input('Enter position: ')
            if coord.isnumeric():
                if int(coord) in range(1, 10) and board[int(coord) - 1] == '-':
                    board[int(coord) - 1] = 'O'
                else:
                    print('Wrong position.')
            else:
                print('Enter a valid number.')
