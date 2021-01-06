import pygame

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
