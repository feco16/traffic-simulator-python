# general
display_width = 400
display_height = 600
lines = 350
columns = 200
start_map_x = 100
start_map_y = 50
base_width = 12

# ball
direction = (5, 1)
ball_yy = 30
ball_xx = int(columns / 2)
ball_size = 5

# handles
handle_width = 40
handle_altitude = 0
space_between_handles = int(handle_width / 5)
left_space = int(columns / 2 - handle_width - space_between_handles / 2)
handle_height = start_map_y + lines

# gameplay
button_pressed = False
handle_delta = 0

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
