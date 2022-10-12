import random
import sys

WIDTH = 8
HEIGHT = 8


def drow_board(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print(f'{y + 1}|', end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print(f'|{y + 1}')
    print(' +--------+')
    print('  12345678')


def get_new_board():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def is_on_board(x, y):
    return 0 <= x <= WIDTH-1 and 0 <= y <= HEIGHT - 1


# Check is move valid and flips opponents tiles
def is_valid_move(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while is_on_board(x, y) and board[x][y] == other_tile:
            x += xdirection
            y += ydirection
            if is_on_board(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])
    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip


def get_board_with_valid_moves(board, tile):
    board_copy = get_board_copy(board)
    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'
    return board_copy


def get_valid_moves(board, tile):
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])
    return valid_moves


def get_score_ofboard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enter_player_tile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('you are playing with X or O')
        tile = input().upper()
        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Human'


def make_move(board, tile, x_start, y_start):
    tiles_to_flip = is_valid_move(board, tile, x_start, y_start)
    if not tiles_to_flip:
        return False
    board[x_start][y_start] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True


# getting board copy for comp
def get_board_copy(board):
    board_copy = get_new_board()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board_copy[x][y] = board[x][y]
    return board_copy


# Checks is move in corner or not
def is_on_corner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def get_player_move(board, player_tile):
    DIGITS_1_TO_8 = ['1', '2', '3', '4', '5', '6', '7', '8']
    while True:
        move = input().lower()
        if move == 'exit' or move == 'help':
            return move
        if len(move) == 2 and move[0] in DIGITS_1_TO_8 and move[1] in DIGITS_1_TO_8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if not is_valid_move(board, player_tile, x, y):
                continue
            else:
                break
        else:
            print('It is not a valid step enter 1-8 for calum and 1-8 for rows')
            print('')
    return [x, y]


def get_computer_move(board, comp_tile):
    possible_move = get_valid_moves(board, comp_tile)
    random.shuffle(possible_move)
    for x, y in possible_move:
        if is_on_corner(x, y):
            return [x, y]
    # Comp will chose move with biggest scores
    best_score = -1
    for x, y in possible_move:
        board_copy = get_board_copy(board)
        make_move(board_copy, comp_tile, x, y)
        score = get_score_ofboard(board_copy)[comp_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score
    return best_move


def print_score(board, player_tile, comp_tile):
    scores = get_score_ofboard(board)
    print(f'Your points are {scores[player_tile]}, computer points are {scores[comp_tile]}')


def play_game(player_tile, comp_tile):
    show_hints = False
    turn = who_goes_first()
    print(f'{turn} is first')
    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        comp_valid_moves = get_valid_moves(board, comp_tile)
        if player_valid_moves == [] and comp_valid_moves == []:
            return board
        elif turn == 'Human':
            if player_valid_moves:
                if show_hints:
                    valid_move = get_board_with_valid_moves(board, player_tile)
                    drow_board(valid_move)
                else:
                    drow_board(board)
                print_score(board, player_tile, comp_tile)
                move = get_player_move(board, player_tile)

                if move == 'exit':
                    print('Thanks for game')
                    sys.exit()
                elif move == 'help':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(board, player_tile, move[0], move[1])
            turn = 'Computer'
        elif turn == 'Computer':
            if comp_valid_moves:
                drow_board(board)
                print_score(board, player_tile, comp_tile)
                input('Press enter to see computer steps ')
                move = get_computer_move(board, comp_tile)
                make_move(board, comp_tile, move[0], move[1])
            turn = 'Human'


print('Hello in game Revesi')

player_tile, comp_tile = enter_player_tile()

while True:
    final_board = play_game(player_tile, comp_tile)
    drow_board(final_board)
    scores = get_score_ofboard(final_board)
    print(f"X has {scores['X']}, O has {scores['O']}")
    if scores[player_tile] > scores[comp_tile]:
        print(f'You have won you have taken {scores[player_tile] - scores[comp_tile]} points')
    elif scores[player_tile] < scores[comp_tile]:
        print(f'you have loose comp have {scores[comp_tile] - scores[player_tile]} points')
    else:
        print('tire')

    print('Do you wont play again?')
    if not input().lower().startswith('y'):
        break
