import pygame
import random
import os

pygame.init()

# Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#Creating Window
screen_width=900
screen_height=600
game_window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,snake_list,snake_size):
    for snake_x,snake_y in snake_list:
        pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])

def welcome():
    exit_game=False
    fps=60
    while not exit_game:
        game_window.fill((200,230,250))
        text_screen("Welcome to Snakes",black,260,250)
        text_screen("Press 'Space' to play",black,255,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# Game Loop
def game_loop():
    # Game Specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 50
    snake_size = 20
    fps = 60
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(100, screen_width - 100)
    food_y = random.randint(100, screen_height - 100)
    score = 0
    snake_list = []
    snake_length = 1

    if(not os.path.exists("hi_score.txt")):
        with open("hi_score.txt","w") as f:
            f.write("0 ")

    with open("hi_score.txt","r") as f:
        hi_score = f.read()

    while not exit_game:
        if game_over:
            with open("hi_score.txt","w") as f:
                f.write(str(hi_score))

            game_window.fill(white)
            text_screen("Game Over! Press Enter to continue...",red,100,250)

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score=score+10
                food_x = random.randint(100, screen_width-100)
                food_y = random.randint(100, screen_height-100)
                snake_length=snake_length+5
                if score>int(hi_score):
                    hi_score=score

            game_window.fill(white)
            text_screen("Score: "+str(score)+"  Hi-Score: "+str(hi_score),red,5,5)
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            plot_snake(game_window,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()