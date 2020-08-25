'''
Tic-tac-toe (American English), noughts and crosses (Commonwealth English), 
or Xs and Os is a paper-and-pencil game for two players, X and O, who take turns 
marking the spaces in a 3×3 grid. The player who succeeds in placing three of their 
marks in a horizontal, vertical, or diagonal row is the winner.
'''

import random


def display_board(board):
    # print('    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('    |   |')
    print('-------------')
    # print('    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('    |   |')
    print('-------------')
    # print('    |   |')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('    |   |')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        print('Player1, do you want X or O?')
        marker = raw_input().upper()

    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def place_marker(board, move, marker):
    board[move] = marker


def win_check(board, marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[9] == marker and board[5] == marker and board[1] == marker))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position1 = ' '

    while position1 not in range(1, 10)or not space_check(board, int(position1)):
        print("Choose your move between position's 1 to 9 :")
        position1 = input()

    return int(position1)


def replay():
    return raw_input('Do you want to play again? Type Yes or No: ').lower().startswith('y')


print("Welcome to Tic-Tac-Toe")
while True:
    theBoard = [' '] * 10
    [player1_marker, player2_marker] = player_input()
    turn = choose_first()
    print(turn + ' goes first!!')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, position, player1_marker)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulation Player 1 you win....")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is a draw!!!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, position, player2_marker)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Congratulation Player2 you win....")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is a draw!!!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
© 2020 GitHub, Inc.
