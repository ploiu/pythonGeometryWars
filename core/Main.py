import pygame
import sys

from Graphics import RendererManager
from Graphics.Entity.PlayerRenderer import PlayerRenderer
from controller import Controller, bind_default_controls_for_player, is_event_controller_input, handle_controller_input
from world import add_entity, update_entities

from world import Player
from time import sleep

# used to reference core game objects (and keep them in memory to prevent them from being garbage collected)
game_registry = {}

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
            game_registry['renderer_manager'].render_game()
        # wait to update the next loop
        clock.tick(desired_fps)


def setup_controllers():
    # create a list of controllers for each joystick PyGame detects
    controllers = [Controller(joystickId) for joystickId in range(pygame.joystick.get_count())]
    game_registry['controllers'] = controllers


def main():
    print('init game')
    pygame.init()
    # screen size
    screen = width, height = 500, 500
    renderer_manager = RendererManager(screen)
    game_registry['renderer_manager'] = renderer_manager
    # DEBUG
    player_renderer = PlayerRenderer()
    renderer_manager.register_renderer(Player, player_renderer)
    player = Player()
    add_entity(player)
    # END DEBUG
    setup_controllers()
    bind_default_controls_for_player(game_registry['controllers'][0], player)
    start_event_loop()


if __name__ == "__main__":
    main()
