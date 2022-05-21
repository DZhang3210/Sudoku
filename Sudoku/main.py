
board1 = [
    [5,8,1,6,7,2,4,3,9],
    [7,9,2,8,4,3,6,5,1],
    [3,6,4,5,9,1,7,8,2],
    [4,3,8,9,5,7,2,1,6],
    [2,5,6,1,8,4,9,7,3],
    [1,7,9,3,2,6,8,4,5],
    [8,4,5,2,1,9,3,6,7],
    [9,1,3,7,6,8,5,2,4],
    [6,2,7,4,3,5,1,9,8]
]
board2 = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]
board3 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
def showSudoku(board):
    for x in range(len(board)):
        for y in range(len(board)):
            print(str(board[x][y]) + " ", end = "")
        print("")



def sudokuVerifier(board):
    for x in range(9):
        for y in range(9):
            pos = (x, y)
            if(not positionCheck(pos, board)):
                return False
    return True

def positionCheck(pos, board):
    # print(checkRow(pos, board))
    # print(checkColumn(pos, board))
    # print(checkSquare(pos, board))
    return (checkRow(pos, board)
           and checkColumn(pos, board)
           and checkSquare(pos, board))

def checkRow(position, board):
    val = board[position[0]][position[1]]
    for i in range(len(board)):
        if(i != position[0]):
            if(val == board[i][position[1]]):
                return False
    return True

def checkColumn(position, board):
    val = board[position[0]][position[1]]
    for i in range(len(board[0])):
        if(i != position[1]):
            if (val == board[position[0]][i]):
                return False
    return True

def checkSquare(position, board):
    square = findSquare(position)
    val = board[position[0]][position[1]]
    for x in range(3):
        for y in range(3):
            newX = x + 3*square[0];
            newY = y + 3* square[1]
            if(not (newX == position[0] and newY == position[1])):
                if(board[newX][newY] == val):
                    return False
    return True

def findSquare(position):
    return (int(position[0]/3), int(position[1]/3))
# showSudoku(board2)
# # print(sudokuVerifier(board2))
# solveSudoku(board2)
# #print (positionCheck((0,0), board1))
# print("\n---------------------\n")
# showSudoku(board2)
# print(sudokuVerifier(board2))