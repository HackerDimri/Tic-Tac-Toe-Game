import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 550))
pygame.display.set_caption("Tic Tac Toe")

zero = pygame.image.load("o.png")
cross = pygame.image.load("x.png")

zero_rect = zero.get_rect()
cross_rect = cross.get_rect()

board = [0] * 9
current_player = 1
game_over = False

def draw_board():
    screen.fill((250, 250, 250))
    
    pygame.draw.line(screen, (0, 0, 0), (133, 0), (133, 550), width=5)
    pygame.draw.line(screen, (0, 0, 0), (266, 0), (266, 550), width=5)
    pygame.draw.line(screen, (0, 0, 0), (0, 183), (400, 183), width=5)
    pygame.draw.line(screen, (0, 0, 0), (0, 366), (400, 366), width=5)
    
    for i in range(9):
        col = i % 3
        row = i // 3
        x = col * 133 + (133 - zero_rect.width) // 2
        y = row * 183 + (183 - zero_rect.height) // 2
        
        if board[i] == 1:
            screen.blit(zero, (x, y))
        elif board[i] == 2:
            screen.blit(cross, (x, y))

def check_winner():
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]

    if all(cell != 0 for cell in board):
        return 0

    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            col = x // 133
            row = y // 183
            index = row * 3 + col
            
            if board[index] == 0:
                board[index] = current_player
                current_player = 3 - current_player

    winner = check_winner()
    if winner is not None:
        if not game_over:
            game_over = True
            if winner == 0:
                print("It's a draw!")
            else:
                print(f"Winner is {'O' if winner == 1 else 'X'}")

    draw_board()
    pygame.display.update()
