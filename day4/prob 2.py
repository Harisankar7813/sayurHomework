'''Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions'''

import random
def start_board():
    return [['*' for i in range(6)] for j in range(6)]

def roll_dice():
    return random.randint(1,6)

def update_board(board,row,col,player,scores):
    if board[row][col]=="*":
        board[row][col]=player
    else:
        scores[player]+=1
        board[row][col]=player
    
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def play():
    board = start_board()
    scores = {'A': 0, 'B': 0}
    while max(scores.values())<5:
        input("Press Enter to roll the dice")
        row_a = roll_dice()
        col_a=roll_dice()
        row_b = roll_dice()
        col_b = roll_dice()
        print(f"player A rolled:{row_a},{col_a}")
        print(f"player B rolled:{row_b},{col_b}")
        update_board(board,row_a-1,col_a-1,'A',scores)
        update_board(board,row_b-1,col_b-1,'B',scores)
        print_board(board)
        print(f"current Score:Player_A:{scores['A']},player_B:{scores['B']}")
        print()
    win=max(scores,key=scores.get)
    print(f"player {win} wins")

if __name__ == "__main__":
    play()

            