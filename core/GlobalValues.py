# when set to false, the game loop will stop but the game will not exit
import pygame

should_run_game_loop = False
# the target refresh rate
desired_fps = 60
# the difficulty modifier. A value greater than 1 will increase the difficulty, while a value between 0 and 1 will
# decrease it
difficulty_modifier = 1
# a list of angles an entity can shoot in
shoot_angles = [0, 45, 90, 135, 180, 225, 270, 315]


def is_running_game_loop():
    return should_run_game_loop


def set_running_game_loop(value):
    global should_run_game_loop
    should_run_game_loop = value
