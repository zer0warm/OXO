import pygame

X = [[(20, 20), (180, 180), (180, 20), (20, 180)], 
     [(220, 20), (380, 180), (380, 20), (220, 180)],
     [(420, 20), (580, 180), (580, 20), (420, 180)],
     [(20, 220), (180, 380), (180, 220), (20, 380)],
     [(220, 220), (380, 380), (380, 220), (220, 380)],
     [(420, 220), (580, 380), (580, 220), (420, 380)],
     [(20, 420), (180, 580), (180, 420), (20, 580)],
     [(220, 420), (380, 580), (380, 420), (220, 580)],
     [(420, 420), (580, 580), (580, 420), (420, 580)]]

O = [[(100, 100), 90],
     [(300, 100), 90],
     [(500, 100), 90],
     [(100, 300), 90],
     [(300, 300), 90],
     [(500, 300), 90],
     [(100, 500), 90],
     [(300, 500), 90],
     [(500, 500), 90]]

screen = None

def draw_board():
    pygame.draw.line(screen, (0, 255, 0), (200, 0), (200, 600))
    pygame.draw.line(screen, (0, 255, 0), (400, 0), (400, 600))
    pygame.draw.line(screen, (0, 255, 0), (0, 200), (600, 200))
    pygame.draw.line(screen, (0, 255, 0), (0, 400), (600, 400))
    pygame.display.flip()

def draw_nought(cellno):
    pygame.draw.circle(screen, (255, 255, 255), *O[cellno], 1)
    pygame.display.flip()

def draw_cross(cellno):
    start, end, start2, end2 = X[cellno]
    pygame.draw.line(screen, (255, 255, 255), start, end, 1)
    pygame.draw.line(screen, (255, 255, 255), start2, end2, 1)
    pygame.display.flip()
