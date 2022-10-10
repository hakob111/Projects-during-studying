import random


def draw_bord(board):
    print(board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')


# Choosing X or O
def player_input():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('please choose X or O ')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# Random chose first player
def first_player():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Humane'


def make_movement(board, letter, movement):
    board[movement] = letter


# Searching winner
def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[5] == le and bo[8] == le and bo[2] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le))


# Game board copy for computer
def bord_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, movement):
    return board[movement] == ' '


def player_move(board):
    movement = ' '
    while movement not in range(1, 10) or not is_space_free(board, int(movement)):
        print('Yor next step (1-9)')
        movement = input()
        return int(movement)


def random_move_choose(board, movement_list):
    possible_movement = []
    for i in movement_list:
        if is_space_free(board, i):
            possible_movement.append(i)
    if len(possible_movement) != 0:
        return random.choice(possible_movement)
    else:
        return None


def computer_movement(board, comp_letter):
    if comp_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        board_copy = bord_copy(board)
        if is_space_free(board_copy, i):
            make_movement(board_copy, comp_letter, i)
            if winner(board_copy, comp_letter):
                return i
    for i in range(1, 10):
        board_copy = bord_copy(board)
        if is_space_free(board_copy, i):
            make_movement(board_copy, player_letter, i)
            if winner(board_copy, player_letter):
                return i

    movement = random_move_choose(board, [1, 3, 7, 9])
    if movement != 0:
        return movement
    if is_space_free(board, 5):
        return 5
    return random_move_choose(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('lets play in X and O')

while True:
    the_Board = [' '] * 10
    player_letter, comp_letter = player_input()
    turn = first_player()
    print('' + turn + ' goes first ')
    game_is_playing = True
    while game_is_playing:
        if turn == 'Humane':
            draw_bord(the_Board)
            movement = player_move(the_Board)
            make_movement(the_Board, player_letter, movement)

            if winner(the_Board, player_letter):
                draw_bord(the_Board)
                print('Hee you are win')
                game_is_playing = False
            else:
                if is_board_full(the_Board):
                    draw_bord(the_Board)
                    print('cove')
                    break
                else:
                    turn = 'Computer'

        else:
            movement = computer_movement(the_Board, comp_letter)
            make_movement(the_Board, comp_letter, movement)

            if winner(the_Board, comp_letter):
                draw_bord(the_Board)
                print('Computer have won')
                game_is_playing = False
            else:
                if is_board_full(the_Board):
                    draw_bord(the_Board)
                    print('cove')
                    break
                else:
                    turn = 'Humane'

    print('Lets play again')
    if not input().lower().startswith('y'):
        break
