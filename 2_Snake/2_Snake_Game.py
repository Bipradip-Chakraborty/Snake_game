#Import the module:
import pygame
import random
import os

#Initialize the following game:
pygame.init()
screen_width = 600
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))

# Colour of the player :
green = (124, 252, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Game specific veriable:
exit_game = False
game_over = False

# Set the font/size of the letter:
font = pygame.font.SysFont(None, 44)


# Bring the score in the display
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

# Start-up windows:
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((255,228,196))
        text_screen('**Welcome to snake game**', red, 95, 200)
        text_screen('--Press Space Bar To Play--', black, 100, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()




        pygame.display.update()
        clock.tick(60)

# # check if hiscore file exists:
# if (not os.path.exists('hiscore')):
#     with open('1.1_Slab Striker_ghiscore', 'w') as f:
#         f.write('0')

#Clock to run the fps:
clock = pygame.time.Clock()

#Function of Game Loop:
def gameloop():
    # Set title:
    pygame.display.set_caption('Snake Game')


    # colour of the food:
    red = (255, 0, 0)

    # Game specific veriable:
    exit_game = False
    game_over = False

    # player connection
    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0

    # Food connection
    food_x = random.randint(0, 4 * screen_width / 5)
    food_y = random.randint(0, 4 * screen_height / 5)
    food_size = 20

    # preparing to increase the length of the snake:
    snake_list = []
    snake_length = 1

    # Increase the velocity of the snake with every score:
    velocity_init = 3


    # Get the score:
    score = 0


    #Set the high score:
    with open('2.1_Snake_Gamescore') as f:
        hiscore = f.read()

    # plotting by increasing the length of the game:
    def plot_snake(gamewindow, color, snake_list, snake_size):
        for x, y in snake_list:
            pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

    while not exit_game:

        #confirm game over
        if game_over:
            gamewindow.fill(black)
            text_screen('Game over! Press enter to continue.', red, 50, 200)

            #Display the high score:
            with open('2.1_Snake_Gamescore', 'w') as f:
                f.write(str(hiscore))

            # Close the game easily:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            #Game controll:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity_init
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity_init
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -velocity_init
                        velocity_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = velocity_init
                        velocity_x = 0

            #Update the position of the snake :
            snake_x  = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # Initialize the score:
            if abs(snake_x - food_x)<11 and abs(snake_y - food_y)<11:
                score = score + 10

                # paste the score:
                if score>int(hiscore):
                    hiscore = score



                # And update the position of the food :
                food_x = random.randint(0, 4 * screen_width / 5)
                food_y = random.randint(0, 4 * screen_height / 5)

                # Increase the snake length :
                snake_length += 5


            with open('2.1_Snake_Gamescore', 'w') as f:
                f.write(str(hiscore))

            #Design the game window:
            gamewindow.fill(green)

            #Draw the score:
            text_screen('score: ' + str(score)+';  Hi-Score : '+ str(hiscore), red, 5, 5)

            #Head of the snake ; connected with the Increase the snake length:
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #Cut the head of the snake :
            if len(snake_list)> snake_length:
                del snake_list[0]

            #check whether there is any collision or not:
            if head in snake_list[:-1]:
                game_over = True

            #limitation of the game i.e. Game over:

            if snake_x<0 or snake_x> screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print('game over')


            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size , snake_size])
            pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size , food_size])

            #Plotting the snake :
            plot_snake(gamewindow, black, snake_list, snake_size)

        #Update the screen:
        pygame.display.update()

        #FPS: Frame Per Second
        clock.tick(60)

    print('Thanks for playing this game.')
    pygame.quit()
    quit()

welcome()
gameloop()