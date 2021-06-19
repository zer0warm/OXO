import pygame
import drawing

screen = None
x_turn = True
done = False
game_board = [''] * 9
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

def initialize(size, caption='Tic-Tac-Toe'):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    screen.fill((0, 0, 0))
    return screen

def quit():
    pygame.quit()

def mainloop():
    global done

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_handler()

def determine_cell(x, y):
    if 0 < y < 200 and 0 < x < 200: return 0
    if 0 < y < 200 and 200 < x < 400: return 1
    if 0 < y < 200 and 400 < x < 600: return 2
    if 200 < y < 400 and 0 < x < 200: return 3
    if 200 < y < 400 and 200 < x < 400: return 4
    if 200 < y < 400 and 400 < x < 600: return 5
    if 400 < y < 600 and 0 < x < 200: return 6
    if 400 < y < 600 and 200 < x < 400: return 7
    if 400 < y < 600 and 400 < x < 600: return 8

def click_handler():
    x, y = pygame.mouse.get_pos()
    cellno = determine_cell(x, y)

    global game_board

    # Only continue when the cell isn't played
    if not bool(game_board[cellno]):
        global x_turn

        if x_turn:
            game_board[cellno] = 'x'
            drawing.draw_cross(cellno)
        else:
            game_board[cellno] = 'o'
            drawing.draw_nought(cellno)

        check_victory()

        x_turn = not x_turn

def check_victory():
    global done

    for comb in win_combinations:
        if x_turn:
            marked_cells = filter(lambda i: game_board[i] == 'x', comb)
        else:
            marked_cells = filter(lambda i: game_board[i] == 'o', comb)

        if tuple(marked_cells) == comb:
            print(f"{'X' if x_turn else 'O'} won!")
            done = True
            return

    # If no victory declared yet the board is full, announce draw
    if all(game_board):
        print("It's a draw!")
        done = True
        return
