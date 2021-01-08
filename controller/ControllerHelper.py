import pygame

from core import get_player
from world.entity.bullet import PlayerBullet
from .SnesMappings import *

"""
A bunch of helper functions for controllers
"""


def bind_default_controls_for_player(controller, player):
    # movement controls
    controller.map_directionalButton(SNESAxes.VERTICAL,
                                     lambda: player.set_velocity_y(player.speed),
                                     lambda: player.set_velocity_y(-player.speed),
                                     lambda: player.set_velocity_y(0)
                                     )
    controller.map_directionalButton(SNESAxes.HORIZONTAL,
                                     lambda: player.set_velocity_x(player.speed),
                                     lambda: player.set_velocity_x(-player.speed),
                                     lambda: player.set_velocity_x(0)
                                     )
    controller.map_button(SNESButtons.X, lambda: PlayerBullet(get_player()).shoot(90), None)
    controller.map_button(SNESButtons.A, lambda: PlayerBullet(get_player()).shoot(0), None)
    controller.map_button(SNESButtons.B, lambda: PlayerBullet(get_player()).shoot(270), None)
    controller.map_button(SNESButtons.Y, lambda: PlayerBullet(get_player()).shoot(180), None)


def is_event_controller_input(event):
    return event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYAXISMOTION


def handle_controller_input(event, controller):
    if event.type == pygame.JOYBUTTONDOWN:
        controller.press_button(event.button)
    elif event.type == pygame.JOYBUTTONUP:
        controller.release_button(event.button)
    elif event.type == pygame.JOYAXISMOTION:
        # call the directional button press on the controller
        controller.press_directionalButton(event.axis, event.value)
