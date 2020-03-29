import pygame

import game_map
import shared

pygame.init()

display_width = 400
display_height = 600

ball_yy = int(shared.lines / 2)
ball_xx = int(shared.columns / 2)

base_width = 3

start_map_x = 100
start_map_y = 50

handle_height = start_map_y + shared.lines

button_pressed = False
handle_delta = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Covid Ball')
clock = pygame.time.Clock()

direction = (1, 1)


def game_loop():
    global button_pressed

    game_map.create_map()

    game_display.fill(green)

    while True:
        game_display.fill(green)
        draw_map(game_map.map_data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        try:
            move_ball()
        except:
            break

        pygame.draw.circle(game_display, black, (ball_xx + start_map_x, ball_yy + start_map_y), 5, 5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            button_pressed = True

        move_handles()
        draw_handles()
        pygame.display.update()
        clock.tick(100000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def move_ball():
    global ball_yy
    global ball_xx
    global direction

    game_map.map_data

    if game_map.map_data[ball_yy + direction[0]][ball_xx + direction[1]] != 0:
        direction = (direction[0] + game_map.map_data[ball_yy + direction[0]][ball_xx + direction[1]][0],
                     direction[1] + game_map.map_data[ball_yy + direction[0]][ball_xx + direction[1]][1] )

    ball_yy += direction[0]
    ball_xx += direction[1]


def move_handles():
    global button_pressed
    global handle_delta

    if button_pressed:
        if handle_delta < (shared.handle_altitude * 0.8):
            handle_delta += 2
        else:
            button_pressed = False
    else:
        if handle_delta > 0:
            handle_delta -= 2


def draw_handles():
    left_handle_start = start_map_x + shared.left_space
    right_handle_start = start_map_x + shared.left_space + shared.handle_width + shared.space_between_handles

    pygame.draw.line(game_display, black, (left_handle_start, handle_height - shared.handle_altitude),
                     (left_handle_start + shared.handle_width, handle_height - handle_delta), base_width)

    pygame.draw.line(game_display, black, (right_handle_start, handle_height - handle_delta),
                     (right_handle_start + shared.handle_width, handle_height - shared.handle_altitude), base_width)


def draw_map(map_data):
    for i in range(0, shared.lines):
        for j in range(0, shared.columns):
            if map_data[i][j] != 0:
                pygame.draw.circle(game_display, black, (j + start_map_x, i + start_map_y), 2, 2)


game_loop()
pygame.quit()
quit()
