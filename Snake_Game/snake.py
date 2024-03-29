import pygame
import time
import random

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game by Geovane Rocha')

clock = pygame.time.Clock()

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,102)
green = (0,255,0)
background = pygame.image.load('green.png')
losed = pygame.image.load('losed.png')
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

x1 = screen_width / 2
y1 = screen_height / 2

x_change = 0
y_change = 0

snake_block = 10
snake_speed = 15

def your_Score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    red_square = True
    
    for x in snake_list:
        if red_square:
            pygame.draw.rect(screen, red, [x[0], x[1], snake_block, snake_block])
            red_square = False
        else:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
            red_square = True
            
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x_change = 0
    y_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.blit(losed, [0,0])
            message("You Lost :( Press Q-Quit or C-Play Again", red)
            your_Score(Length_of_snake - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0 :
            game_close = True

        x1 += x_change
        y1 += y_change

        screen.blit(background, [0,0])
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        your_Score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

