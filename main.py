#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from chess.board import Board, WHITE, BLACK, width, height, \
    square_size, col, row

from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, \
    KEYDOWN, QUIT

from chess.PieceMoves import *


# hello waithyboy
# Hello1234
# main function

def main():
    window = pygame.display.set_mode((width, height))
    window.fill((125, 125, 125))

    pygame.init()

    board = Board()
    moveList = [] # returns all possible moves, for a single piece; changes each turn (black vs. white)
    running = True

    # loadImages();

    while running:
        pygame.event.pump()
        if board.checkMate():
            s = ('Black Wins!' if board.whiteToMove else 'White Wins!')
            print(s)
            break
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # returns location of the mouse as a tuple (#, #) --> (x, y)
                column = location[0] // square_size
                rownum = location[1] // square_size
                # if statement only runs if you click on the same piece twice
                if board.selected_piece == (rownum, column):
                    board.selected_piece = ()
                    board.selected_squares = []
                else:
                    board.selected_piece = (rownum, column)
                    # selected squares follows a format like this: [(selected piece), (destination)]
                    board.selected_squares.append(board.selected_piece)
                # executed if there is only one move added (square selected, but no origin selected)
                if len(board.selected_squares) == 1:
                    # if the square at rownum, column is not empty, this will be executed
                    if board.chessBoard[board.selected_piece[0]][board.selected_piece[1]] != '--':
                        # showMoves returns all possible moves for that piece
                        moveList = board.showMoves(rownum, column,
                                board.selected_piece)
                
                # if selected squares has an origin and destination
                elif len(board.selected_squares) == 2:
                    # check from above
                    if board.chessBoard[board.selected_squares[0][0]][board.selected_squares[0][1]] \
                        != '--':
                        board.move(board.selected_squares[0],
                                   board.selected_squares[1], moveList)
                        board.selected_piece = ()
                        board.selected_squares = []
                    else:
                        board.selected_squares = []
                        board.selected_squares.append(board.selected_piece)
                        board.selected_piece = ()
                    moveList = []
            elif event.type == KEYDOWN:
                if pressed_keys[K_ESCAPE]:
                    running = False
                elif pressed_keys[K_LEFT]:
                    board.undo()

        board.load_images()
        window.fill((125, 125, 125))

        board.draw_squares(window)
        board.draw_pieces(window)
        for move in moveList:
            pygame.draw.circle(window, (150, 0, 0), ((move[1] + 0.5)
                               * square_size, (move[0] + 0.5)
                               * square_size), 10, 100)

            # .draw.circle --> (window, color, x --> column, y --> row, radius)

            # running=False

        pygame.display.flip()


          # print(pressed_keys)

if __name__ == '__main__':
    main()


pygame.quit()

# .checkMate()
# .showMoves
# .move()
# .undo()
# .load_images() --> not important for now
# .draw_pieces
