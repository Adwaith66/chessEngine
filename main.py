    
import pygame

from chess.board import (Board,WHITE, BLACK, width, height, square_size, 
    col, row)

from pygame.locals import (K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, 
    KEYDOWN, QUIT)


def main():
    window = pygame.display.set_mode((width, height))
    window.fill((125,125,125))

 
    pygame.init()

    board = Board()

    running = True
    #loadImages();
    while running:
        pygame.event.pump()

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                column = location[0]//square_size
                rownum = location[1]//square_size
                if board.selected_piece == (rownum, column):
                    board.selected_piece = ()
                    board.selected_squares = []
                else:
                    board.selected_piece = (rownum, column)
                    board.selected_squares.append(board.selected_piece)
                if len(board.selected_squares)==2:
                    board.move(board.selected_squares[0], board.selected_squares[1])
                    board.selected_piece = ()
                    board.selected_squares = []
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    

        board.load_images()
        board.draw_squares(window)
        board.draw_pieces(window)
        pygame.display.flip()
        


if __name__ == '__main__':
    main()

print("ending")
pygame.quit()

