import drawing
import pygame
import game

if __name__ == '__main__':
    screen = game.initialize()
    drawing.screen = screen
    drawing.draw_board()
    game.screen = screen
    game.mainloop()
