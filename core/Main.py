import sys

import pygame

from Graphics import RendererManager, register_renderers, register_images
from controller import Controller, bind_default_controls_for_player, is_event_controller_input, handle_controller_input
from core import difficulty_modifier

from core.Utils import game_registry
from event import process_event, register_event_handlers, LEVEL_START_EVENT, LEVEL_PROGRESS_EVENT
from world import add_entity, update_entities, Player
from world.entity.enemy import Triangle, Square, Circle


def start_event_loop():
    from core.GlobalValues import is_running_game_loop, set_running_game_loop, desired_fps
    global desired_fps
    clock = pygame.time.Clock()
    # TODO a lot of this should be moved out, but to where?
    pygame.time.set_timer(LEVEL_PROGRESS_EVENT, int(10_000 // difficulty_modifier))
    set_running_game_loop(True)
    # set up an initial level
    pygame.event.post(pygame.event.Event(LEVEL_START_EVENT))
    while True:
        if is_running_game_loop():
            update_entities()
        else:
            # stop the timer for level progress
            pygame.time.set_timer(LEVEL_PROGRESS_EVENT, 0)
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
    from event.handlers import entity_handlers, level_handlers, player_handlers
    # entity handlers
    for event_id, handler_list in entity_handlers.items():
        register_event_handlers(event_id, handler_list)
    # level handlers
    for event_id, handler_list in level_handlers.items():
        register_event_handlers(event_id, handler_list)
    # player handlers
    for event_id, handler_list in player_handlers.items():
        register_event_handlers(event_id, handler_list)


def register_enemies():
    from world.entity.enemy import register_enemy
    register_enemy(Triangle, 2)
    register_enemy(Square, 2)
    register_enemy(Circle, 5)


def register_powerups():
    from world.entity.powerup import register_powerup, HealthPowerupEntity
    register_powerup(HealthPowerupEntity)


def setup_player():
    player = Player()
    add_entity(player)
    game_registry['player'] = player


def main():
    print('init game')
    pygame.init()
    game_registry['renderer_manager'] = RendererManager()
    setup_player()
    register_enemies()
    register_images()
    register_renderers()
    register_powerups()
    setup_controllers()
    register_all_event_handlers()
    bind_default_controls_for_player(game_registry['controllers'][0], game_registry['player'])
    start_event_loop()
