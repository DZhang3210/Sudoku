import pygame
from pygame.locals import *
from main import *

pygame.init()
display_width = 603
display_height = 700
dif = display_width//9
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sudoku")
game_display.fill((194,194,214))
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 16)
currentX = 0
currentY = 0
flag = (0,0)

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
for x in range(len(board2)):
    for y in range(len(board2)):
        if(board2[x][y] != 0):
            valid[x][y] = 1
#board = int[9][9]

def event_handler():
    for event in pygame.event.get():
        if(event.type == QUIT or (
            event.type == KEYDOWN and (
            event.key == K_ESCAPE or
            event.key == K_q
        ))):
            pygame.quit()
            quit()
        if ((event.type == KEYDOWN and event.key == K_d)):
            pygame.quit()
            quit()


def drawSudoku(board):
    for x in range(9):
        for y in range(9):
            if(board[x][y] != 0):
                pygame.draw.rect(game_display, (0, 155,155) , [dif * x , dif * y , dif, dif], 0)
                text1 = font.render(str(board[x][y]), 1, (0, 0, 0))
                game_display.blit(text1, (x * dif + 15, y * dif + 15))
            pygame.draw.rect(game_display, (0, 0, 0), [dif * x , dif * y , dif, dif], 2)

    pygame.draw.line(game_display, (0, 0, 0), (0, display_width), (800,display_width), 2)
    text2 = font1.render("Press R to reset\t"
                         "Press D to automatically Solve\t"
                         "Press F if you finish\t", 1, (0,0,0))
    game_display.blit(text2, (20, display_width))
    #drawing bold lines
    boldness = 10;
    pygame.draw.line(game_display, (0, 0, 0), (0, 0), (0, display_width), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (display_width//3, 0), (display_width//3, display_width), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (2*display_width//3, 0), (2*display_width//3, display_width), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (display_width, 0), (display_width, display_width), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (0, 0), (display_width, 0), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (0, display_width//3), (display_width, display_width//3), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (0, 2*display_width//3), (display_width, 2*display_width//3), boldness)
    pygame.draw.line(game_display, (0, 0, 0), (0, display_width), (display_width, display_width), boldness)

drawSudoku(board2)

def delete():
    pygame.draw.rect(game_display, (194,194,214), [currentX, currentY, dif, dif], 0)
    pygame.draw.rect(game_display, (51, 153, 255), [currentX, currentY, dif, dif], 2)
    board2[currentX // dif][currentY // dif] = 0


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
            pygame.draw.rect(game_display, (194,194,214), [x*dif, y*dif, dif, dif], 0)
            pygame.draw.rect(game_display, (255, 0, 0), [x*dif, y*dif, dif, dif], 2)
            board2[x][y] = 0

    pygame.draw.rect(game_display, (194,194,214), [x*dif, y*dif, dif, dif], 0)
    pygame.draw.rect(game_display, (255, 0, 0), [x*dif, y*dif, dif, dif], 2)
    board2[x][y] = 0
    return False

while True:
    pos = pygame.mouse.get_pos()
    if(pos[1] < display_width):
        squareX = (pos[0] // dif) * dif
        squareY = (pos[1] // dif) * dif
        if (squareX != currentX or squareY != currentY):
            pygame.draw.rect(game_display, (0, 0, 0), [currentX, currentY, dif, dif], 2)
            pygame.draw.rect(game_display, (255, 255, 0), [squareX, squareY, dif, dif], 2)
            currentX, currentY = squareX, squareY
        for event in pygame.event.get():

        #Check if you need to quit program
            if (event.type == QUIT or (
                    event.type == KEYDOWN and (
                    event.key == K_ESCAPE or
                    event.key == K_q
            ))):
                pygame.quit()
                quit()
            if (event.type == KEYDOWN and event.key == K_f):
                solveSudoku(board2)
        #Check for in case you need to insert number
            if(event.type == KEYDOWN):
                val = 0
                if(event.key == K_1):
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
                elif(event.key == K_g):
                    val = 10
                elif(event.key == K_r):
                    val = 11
                elif (event.key == K_h):
                    val = 12
                checkX = currentX // dif
                checkY = currentY // dif
                if(valid[checkX][checkY] != 1):
                    if (val == 10):
                        delete()
                    elif (val == 11):
                        game_display.fill((194, 194, 214))
                        drawSudoku(reset)
                    elif (val == 12):
                        game_display.fill((194, 194, 214))
                        drawSudoku(empty)
                    elif(val != 0):
                        board2[currentX // dif][currentY // dif] = val
                        if (positionCheck((checkX, checkY), board2)):
                            text2 = font.render(str(val), 1, (0, 0, 0))
                            game_display.blit(text2, (currentX + dif // 4, currentY + dif // 4))
                        else:
                            pygame.draw.rect(game_display, (255, 0, 0), [currentX, currentY, dif, dif], 2)
                            board2[currentX // dif][currentY // dif] = 0
    event_handler()
    pygame.display.update()

