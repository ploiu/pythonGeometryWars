import pygame
import sys

from Graphics import RendererManager
from Graphics.Entity.PlayerRenderer import PlayerRenderer
from controller import Controller
from world import add_entity, update_entities

# used to reference core game objects (and keep them in memory to prevent them from being garbage collected)
from world import Player

game_registry = {}


def start_event_loop():
    while True:
        for event in pygame.event.get():
            # allow the user to exit the game
            if event.type == pygame.QUIT:
                sys.exit(0)
            else:
                update_entities()
                game_registry['renderer_manager'].render_game()


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
    print(game_registry)
    start_event_loop()


if __name__ == "__main__":
    main()
