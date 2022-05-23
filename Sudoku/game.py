import pygame
from pygame.locals import *
from main import *

pygame.init()
pygame.display.set_caption("Sudoku")
display_width, display_height = 603, 700
game_display = pygame.display.set_mode((display_width, display_height))
game_display.fill((194,194,214))
dif = display_width//9
font, font1 = pygame.font.Font('freesansbold.ttf', 32), pygame.font.Font('freesansbold.ttf', 16)
currentX, currentY = 0,0


empty = [
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
reset = [
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
valid = [
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

#Initialize Array
for x in range(len(board2)):
    for y in range(len(board2)):
        if(board2[x][y] != 0):
            valid[x][y] = 1

#Update for relevent use
def event_handler(currentX, currentY):
        for event in pygame.event.get():
            if (event.type == QUIT or (
                    event.type == KEYDOWN and (
                    event.key == K_ESCAPE or
                    event.key == K_q
            ))):
                pygame.quit()
                quit()
            # Check for in case you need to insert number
            if (event.type == KEYDOWN):
                val = 0
                if (event.key == K_1):
                    val = 1
                elif (event.key == K_2):
                    val = 2
                elif (event.key == K_3):
                    val = 3
                elif (event.key == K_4):
                    val = 4
                elif (event.key == K_5):
                    val = 5
                elif (event.key == K_6):
                    val = 6
                elif (event.key == K_7):
                    val = 7
                elif (event.key == K_8):
                    val = 8
                elif (event.key == K_9):
                    val = 9
                elif (event.key == K_g):
                    val = 10
                elif (event.key == K_r):
                    val = 11
                elif (event.key == K_h):
                    val = 12
                elif(event.key == K_d):
                    val = 13
                elif(event.key == K_f):
                    val = 14
                checkX = currentX // dif
                checkY = currentY // dif
                if (valid[checkX][checkY] != 1):
                    if (val == 10):

                        delete(currentX, currentY, board2)
                    elif (val == 11):
                        game_display.fill((194, 194, 214))
                        drawSudoku(reset)
                        for x in range(len(board2)):
                            for y in range(len(board2)):
                                if(valid[x][y] == 0):
                                    board2[x][y] = 0
                    elif (val == 12):
                        game_display.fill((194, 194, 214))
                        drawSudoku(empty)
                        for x in range(len(board2)):
                            for y in range(len(board2)):
                                board2[x][y] = 0
                                valid[x][y] = 0
                    elif(val == 13):
                        sudokuVerifier(board2)
                    elif(val == 14):
                        game_display.fill((194, 194, 214))
                        drawSudoku(reset)
                        for x in range(len(board2)):
                            for y in range(len(board2)):
                                if (valid[x][y] == 0):
                                    board2[x][y] = 0
                        solveSudoku(board2)
                    elif (board2[currentX // dif][currentY // dif] == 0 and val != 0):
                        board2[currentX // dif][currentY // dif] = val
                        if (positionCheck((checkX, checkY), board2)):
                            text2 = font.render(str(val), 1, (0, 0, 0))
                            game_display.blit(text2, (currentX + dif // 4, currentY + dif // 4))
                        else:
                            pygame.draw.rect(game_display, (255, 0, 0), [currentX, currentY, dif, dif], 2)
                            board2[currentX // dif][currentY // dif] = 0

def drawSudoku(board):
    #Read in board and fill-in spaces
    for x in range(len(board)):
        for y in range(len(board)):
            if(board[x][y] != 0):
                pygame.draw.rect(game_display, (0, 155,155) , [dif * x , dif * y , dif, dif], 0)
                text1 = font.render(str(board[x][y]), 1, (0, 0, 0))
                game_display.blit(text1, (x * dif + 15, y * dif + 15))
            pygame.draw.rect(game_display, (0, 0, 0), [dif * x , dif * y , dif, dif], 2)

    #Read-In Text
    pygame.draw.line(game_display, (0, 0, 0), (0, display_width), (800,display_width), 2)
    text2 = font1.render("Press R to reset\t"
                         "Press G to delete \t"
                         "Press H to blank out puzzle \t", 1, (0,0,0))
    game_display.blit(text2, (20, display_width))
    text2 = font1.render("Press D to Verify if it has been solved\t"
                         "Press F to automatically solve\t", 1, (0, 0, 0))
    game_display.blit(text2, (20, display_width + 32))

#Optimize for better widespread use
def delete(x, y, board):
    pygame.draw.rect(game_display, (194,194,214), [x, y, dif, dif], 0)
    pygame.draw.rect(game_display, (51, 153, 255), [x, y, dif, dif], 2)
    board[x // dif][y // dif] = 0

def solveSudoku(board):
    helperMethod(0, 0, board)
def helperMethod(x, y, board):
    # print("x: " + str(x) + " y: " + str(y))
    currentX, currentY = x, y
    if (y == 9):
        return True
    if (x > 8):
        return helperMethod(0, y + 1, board)
    if (board[x][y] != 0):
        return helperMethod(x + 1, y, board)
    for i in range(1, 10):
        board[x][y] = i

        if (positionCheck((x, y), board)):
            pygame.display.update()
            pygame.time.delay(50)
            text2 = font.render(str(i), 1, (0, 0, 0))
            pygame.draw.rect(game_display, (0, 204, 0), [x * dif, y * dif, dif, dif], 2)
            game_display.blit(text2, (x*dif + dif // 4, y*dif + dif // 4))
            if (helperMethod(x + 1, y, board)):
                return True
            # Add at Location
            delete(x*dif, y*dif, board2)

    delete(x*dif, y*dif, board2)
    return False

def sudokuVerifier(board):
    for x in range(len(board2)):
        for y in range(len(board2)):
            pos = (x, y)
            if(board[x][y] != 0 and positionCheck(pos, board)):
                pygame.time.delay(20)
                pygame.display.update()
                pygame.draw.rect(game_display, (198, 49,212) , [dif * x , dif * y , dif, dif], 2)
            else:
                pygame.draw.rect(game_display, (255, 0, 0), [dif * x, dif * y, dif, dif], 2)
                return
    return True








#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#START OF MAIN FUNCTION
drawSudoku(board2)
while True:
    #Constantly checking for mouse movement to indicate where it's highlighting over
    pos = pygame.mouse.get_pos()
    if (pos[1] < display_width):
        squareX = (pos[0] // dif) * dif
        squareY = (pos[1] // dif) * dif
        if (squareX != currentX or squareY != currentY):
            pygame.draw.rect(game_display, (0, 0, 0), [currentX, currentY, dif, dif], 2)
            pygame.draw.rect(game_display, (255, 255, 0), [squareX, squareY, dif, dif], 2)
            currentX, currentY = squareX, squareY

    event_handler(currentX, currentY)
    pygame.display.update()

