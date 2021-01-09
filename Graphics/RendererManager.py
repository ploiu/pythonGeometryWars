import pygame

# the screen background color
from core import get_player
from world import EntityManager

screen_background = 0, 0, 0


class RendererManager:
    # the list of all renderers in the game, denoted by a class reference followed by a renderer
    registered_renderers = {}
    screen = None

    def __init__(self):
        global screen_size
        screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        RendererManager.screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)

    @staticmethod
    def register_renderer(entity_type, renderer):
        RendererManager.registered_renderers[entity_type] = renderer

    @staticmethod
    def get_renderer(entity_type=None):
        if RendererManager.registered_renderers[entity_type] is not None:
            return RendererManager.registered_renderers[entity_type]
        else:
            raise ValueError("No renderer for {0}".format(entity_type))

    def render_game(self):
        """
        Renders everything in the game
        """
        self.render_background()
        self.render_world_objects()
        self.render_entities()
        self.render_player_health()
        pygame.display.flip()

    def render_background(self):
        self.screen.fill(screen_background)
        # TODO maybe render other things like menus n stuff

    def render_world_objects(self):
        pass  # TODO

    def render_entities(self):
        for entity in EntityManager.entities:
            renderer_type = type(entity)
            self.registered_renderers[renderer_type].render(entity)

    @staticmethod
    def render_player_health():
        player = get_player()
        font = pygame.font.SysFont(None, 20)
        img = font.render("Health: {0}".format(player.current_health), True, (255, 0, 0))
        RendererManager.screen.blit(img, (20, screen_size[1] - 20))
