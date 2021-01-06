import sys

import pygame

from Graphics import RendererManager, register_renderers
from controller import Controller, bind_default_controls_for_player, is_event_controller_input, handle_controller_input
from core.Utils import game_registry
from event import process_event, register_event_handlers
from world import add_entity, update_entities, Player

# used to reference core game objects (and keep them in memory to prevent them from being garbage collected)
from world.entity.enemy import Triangle

# TODO move to a config file in some way
desired_fps = 60


def start_event_loop():
    clock = pygame.time.Clock()
    while True:
        update_entities()
        for event in pygame.event.get():
            # allow the user to exit the game
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif is_event_controller_input(event):
                handle_controller_input(event, game_registry['controllers'][event.joy])
            else:
                process_event(event)
            game_registry['renderer_manager'].render_game()
        # wait to update the next loop
        clock.tick(desired_fps)


def setup_controllers():
    # create a list of controllers for each joystick PyGame detects
    controllers = [Controller(joystickId) for joystickId in range(pygame.joystick.get_count())]
    game_registry['controllers'] = controllers


def register_all_event_handlers():
    from event.handlers import entity_handlers
    for event_id, handler_list in entity_handlers.items():
        register_event_handlers(event_id, handler_list)


def setup_player():
    player = Player()
    add_entity(player)
    game_registry['player'] = player


def main():
    print('init game')
    pygame.init()
    # screen size
    screen = 500, 500
    game_registry['renderer_manager'] = RendererManager(screen)
    # DEBUG
    triangle = Triangle()
    triangle.pos_x = 100
    triangle.pos_y = 100
    add_entity(triangle)
    # END DEBUG
    setup_player()
    register_renderers()
    setup_controllers()
    register_all_event_handlers()
    bind_default_controls_for_player(game_registry['controllers'][0], game_registry['player'])
    start_event_loop()


if __name__ == "__main__":
    main()
