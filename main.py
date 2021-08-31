    
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

        if pressed_keys[K_ESCAPE]:
            running = False

        board.draw_squares(window)
        board.load_images()
        board.draw_pieces(window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
pygame.quit()

