#!/bin/python3

def nextMove(posr, posc, board):
    for i in range(5):
        if 'd' in board[i]:
            x = i
            y = board[i].index('d')
    c_diff = y-posc
    r_diff = x-posr
    
    if c_diff>0:
        print('RIGHT')
    elif c_diff<0:
        print('LEFT')
    elif r_diff>0:
        print('DOWN')
    elif r_diff<0:
        print('UP')
    else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
    
    
    
'''
Sample Input

0 0
b---d
-----
-----
-----
-----

Output Format

Output is the action that is taken by the bot in the current step and it can be any of the movements in 4 directions or cleaning the cell in which it is currently located. The output formats are LEFT, RIGHT, UP and DOWN or CLEAN. Output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.

Sample Output

RIGHT

'''
