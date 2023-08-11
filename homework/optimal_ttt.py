board = [*'-' * 9]
check = ['012', '345', '678', '036', '147', '258', '048', '246']


def draw_board(board):
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
    # showing optimal moves
    if for_x:
        scores = map(lambda c: {-2: '-', -1: 'L', 0: 'D', 1: 'W', 2: '-'}[c], scores)
    else:
        scores = map(lambda c: {-2: '-', -1: 'W', 0: 'D', 1: 'L', 2: '-'}[c], scores)
    play(for_x, scores)


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


def play(player_x, scores):
    draw_board(board)
    print('========================')
    draw_board(list(scores))
    coord = input(f"Enter position for {'X' if player_x else 'O'} (1-9): ")
    if coord.isdecimal() and int(coord) in range(1, 10) and board[int(coord) - 1] == '-':
        board[int(coord) - 1] = 'X' if player_x else 'O'
        if not is_game_over(board):
            make_best_move(not player_x)
    else:
        print('Not a valid number.')


while True:
    game_over = is_game_over(board)
    if game_over:
        draw_board(board)
        print("It's a tie!" if game_over == 'tie' else 'The computer won!')
        break
    else:
        print('W = win, D = draw, L = lose')
        play('X', [*'D' * 9])
