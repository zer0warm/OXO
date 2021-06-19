import drawing
import pygame
import game

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic-Tac-Toe')
    screen.fill((0, 0, 0))
    return screen

if __name__ == '__main__':
    screen = initialize()
    drawing.screen = screen
    drawing.draw_board()
    game.screen = screen
    game.mainloop()
