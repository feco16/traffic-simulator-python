import random

import pygame
import shared
import simulate

from shared import cells

pygame.init()

display_width = 1500
display_height = 400

car_width = 30
road_height = 40
road_y = 100

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Traffic simulator')
clock = pygame.time.Clock()

car_img = pygame.image.load('car.jpg')
car_img = pygame.transform.scale(car_img, (car_width - 2, 20))


def car(x, y):
    game_display.blit(car_img, (x, y))


def road(y):
    pygame.draw.rect(game_display, white, pygame.Rect((0, y), (display_width, road_height * shared.lines)))

    pygame.draw.line(game_display, black, (0, y), (display_width, y), 3)
    for lines in range(1, shared.lines + 1):
        pygame.draw.line(game_display, black, (0, y + lines * road_height), (display_width, y + lines * road_height), 2)

    pygame.draw.line(game_display, black, (0, y + shared.lines * road_height),
                     (display_width, y + shared.lines * road_height), 3)

    for cell in range(0, shared.columns):
        pygame.draw.line(game_display, black, (cell * car_width, y),
                         (cell * car_width, y + road_height * shared.lines))


def draw_map():
    game_display.fill(green)
    road(100)


def game_loop():

    while shared.finished_cars < 1000:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(shared.cells)
                shared.print_statistics()
                pygame.quit()
                quit()

        draw_map()

        simulate.one_clock()
        # print(cells)

        for line in range(0, shared.lines):
            for cell in range(0, shared.columns):
                if type(cells[line][cell]) == tuple:
                    car(cell * car_width + 1, road_y + road_height * line + 5)

        pygame.display.update()
        clock.tick(10)

    shared.print_statistics()


game_loop()
pygame.quit()
quit()
