import drawing
import pygame
import game

if __name__ == '__main__':
    screen = game.initialize(size=(600, 600))
    drawing.screen = screen
    drawing.draw_board()
    game.screen = screen
    game.mainloop()
