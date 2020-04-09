import pygame

import game_map
import shared

pygame.init()

game_display = pygame.display.set_mode((shared.display_width, shared.display_height))
pygame.display.set_caption('Covid Ball')
clock = pygame.time.Clock()


def game_loop():
    """ Loop until the game is exited"""
    game_map.create_map()

    while True:
        game_display.fill(shared.green)
        draw_map()
        # try:
        game_map.move_ball()
        # except:
        #     print("STOP THE GAME. THE BALL CANNOT BE MOVED")
        #     break
        draw_ball()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            button_pressed = True

        move_handles()
        draw_handles()
        pygame.display.update()

        check_if_exited()

        # pygame.time.wait(10)
        clock.tick(500)

    while True:
        check_if_exited()




def move_handles():
    """ Move handles according to the buttons pressed"""
    if shared.button_pressed:
        if shared.handle_delta < (shared.handle_altitude * 0.8):
            shared.handle_delta += 2
        else:
            shared.button_pressed = False
    else:
        if shared.handle_delta > 0:
            shared.handle_delta -= 2


def draw_handles():
    left_handle_start = shared.start_map_x + shared.left_space
    right_handle_start = shared.start_map_x + shared.left_space + shared.handle_width + shared.space_between_handles

    pygame.draw.line(game_display, shared.black,
                     (left_handle_start, shared.handle_height - shared.handle_altitude),
                     (left_handle_start + shared.handle_width,
                      shared.handle_height - shared.handle_delta),
                     shared.base_width)

    pygame.draw.line(game_display, shared.black,
                     (right_handle_start, shared.handle_height - shared.handle_delta),
                     (right_handle_start + shared.handle_width,
                      shared.handle_height - shared.handle_altitude), shared.base_width)


def draw_map():
    for i in range(0, shared.lines):
        for j in range(0, shared.columns):
            if game_map.map_data[i][j] != 0:
                pygame.draw.circle(game_display, shared.black,
                                   (j + shared.start_map_x, i + shared.start_map_y), 2, 2)


def draw_ball():
    pygame.draw.circle(game_display, shared.black,
                       (shared.ball_xx + shared.start_map_x, shared.ball_yy + shared.start_map_y),
                       shared.ball_size, shared.ball_size)


def check_if_exited():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


game_loop()
pygame.quit()
quit()
