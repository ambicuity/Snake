import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize the snake
snake_list = []
snake_length = 1

# Initial position and direction of the snake
snake_head = [width // 2, height // 2]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed_controller = pygame.time.Clock()

# Food position
food_position = [random.randrange(1, (width//10)) * 10,
                 random.randrange(1, (height//10)) * 10]

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to display text
def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

# Function to display messages
def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (width / 2, height / 2)
    display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)

# Function to start the game
def game():
    global snake_head, snake_direction, change_to, snake_speed, snake_list, snake_length, food_position

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        # Change the snake's direction
        if change_to == "UP" and not snake_direction == "DOWN":
            snake_direction = "UP"
        elif change_to == "DOWN" and not snake_direction == "UP":
            snake_direction = "DOWN"
        elif change_to == "LEFT" and not snake_direction == "RIGHT":
            snake_direction = "LEFT"
        elif change_to == "RIGHT" and not snake_direction == "LEFT":
            snake_direction = "RIGHT"

        # Move the snake
        if snake_direction == "UP":
            snake_head[1] -= snake_block
        elif snake_direction == "DOWN":
            snake_head[1] += snake_block
        elif snake_direction == "LEFT":
            snake_head[0] -= snake_block
        elif snake_direction == "RIGHT":
            snake_head[0] += snake_block

        # Game over if snake hits the boundaries
        if (
            snake_head[0] >= width
            or snake_head[0] < 0
            or snake_head[1] >= height
            or snake_head[1] < 0
        ):
            game_over = True

        # Game over if snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Move the snake
        snake_list.append(list(snake_head))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Draw the snake and food
        display.fill(black)
        our_snake(snake_block, snake_list)
        pygame.draw.rect(display, red, [food_position[0], food_position[1], snake_block, snake_block])

        pygame.display.update()

        # Generate a new food position if snake eats the food
        if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
            food_position = [random.randrange(1, (width//10)) * 10,
                             random.randrange(1, (height//10)) * 10]
            snake_length += 1

        # Control snake speed
        snake_speed_controller.tick(snake_speed)

    # Quit the game
    pygame.quit()

# Function to create a start window
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(black)
        large_text = pygame.font.Font('freesansbold.ttf', 80)
        text_surf, text_rect = text_objects("Snake Game", large_text)
        text_rect.center = (width / 2, height / 4)
        display.blit(text_surf, text_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button_rect = pygame.Rect(width/2 - 100, height/2, 200, 50)
        pygame.draw.rect(display, green, button_rect)
        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf, text_rect = text_objects("Start", small_text)
        text_rect.center = ((width / 2), (height / 2) + 25)
        display.blit(text_surf, text_rect)

        if button_rect.collidepoint(mouse):
            if click[0] == 1:
                intro = False
                game()

        pygame.display.update()

# Start the game intro
game_intro()
