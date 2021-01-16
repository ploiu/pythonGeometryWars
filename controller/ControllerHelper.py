import pygame

from core import get_player
from world.entity.bullet import PlayerBullet
from .SnesMappings import SNESButtons
import sys

if sys.platform == 'win32':
    from .SnesMappings import SNESAxes_Win as SNESAxes
else:
    from .SnesMappings import SNESAxes

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
    controller.map_button(SNESButtons.X, lambda: player.update_shooting_angle(90),
                          lambda: player.update_shooting_angle(-90))
    controller.map_button(SNESButtons.A, lambda: player.update_shooting_angle(0),
                          lambda: player.update_shooting_angle(-1))
    controller.map_button(SNESButtons.B, lambda: player.update_shooting_angle(270),
                          lambda: player.update_shooting_angle(-270))
    controller.map_button(SNESButtons.Y, lambda: player.update_shooting_angle(180),
                          lambda: player.update_shooting_angle(-180))
    # powerups
    controller.map_button(SNESButtons.L_BUMPER, lambda: player.consume_powerup(index=0), None)
    controller.map_button(SNESButtons.R_BUMPER, lambda: player.consume_powerup(index=1), None)


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
