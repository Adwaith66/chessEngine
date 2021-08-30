    
import pygame

from chess.constants import (WHITE, BLACK, width, height, square_size, 
    col, row)

from chess.board import Board

from pygame.locals import (K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, 
    KEYDOWN, QUIT)


def main():
    window = pygame.display.set_mode((width, height))

    pygame.init()

    board = Board()

    print("BASED")
    running = True
    #loadImages();
    while running:
        pygame.event.pump()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_ESCAPE]:
            running = False

        board.draw_squares(window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
pygame.quit()

