import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)


def coli(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (200, 200)]
snake_cor = pygame.Surface((10,10))
snake_cor.fill((255,255,255))


laranja_pos = on_grid_random()
laranja_cor = pygame.Surface((10,10))
laranja_cor.fill((255,165,0))


direcao = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',18)
pontos = 0

game_over = False
while not game_over:
    clock.tick(19)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN: 
                direcao = UP
            elif event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            elif event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            elif event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT           

    if coli(snake[0], laranja_pos):
        laranja_pos = on_grid_random()
        snake.append((0,0))
        pontos = pontos +1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake [0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) -1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break


    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif direcao  == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif direcao  == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif direcao  == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(laranja_cor, laranja_pos)

    for x in range(0, 600, 10 ):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10,):
        pygame.draw.line(screen, (40, 40, 40 ), (0, y), (600, y))
    
    score_font  = font.render('Pontos: %s' % (pontos), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_cor,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('PERDEU kk', True, (255,255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            