import math

def update_position(posr, posc, dirties):
    nearest_dirt = []
    for i in range(len(dirties)):
        # Euclidean distance
        result = math.sqrt(((dirties[i][0] - posr) ** 2) + ((dirties[i][1] - posc) ** 2))
        nearest_dirt.append(result)
    return [x for (y,x) in sorted(zip(nearest_dirt,dirties))]    

# Set the bot in your new position
def next_move(posr, posc, x, y, board):
    dirties = []
    for i in range(x):
        for j in range(y):
            if board[i][j] == 'd':
                dirties.append([i, j])
    next_dirt = update_position(posr, posc, dirties)
    if next_dirt[0][1] < posc:
        print('LEFT')
    elif next_dirt[0][1]  > posc:
        print('RIGHT')
    elif next_dirt[0][0] < posr:
        print('UP')
    elif next_dirt[0][0] > posr:
        print('DOWN')
    else:
        print('CLEAN')
        
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
    
    
    
'''
Sample Input

0 0
5 5
b---d
-d--d
--dd-
--d--
----d

Sample Output

RIGHT

'''
