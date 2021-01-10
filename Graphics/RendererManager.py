import pygame

# the screen background color
from core import get_player
from world import EntityManager

screen_background = 0, 0, 0
screen_size = None


class RendererManager:
    # the list of all renderers in the game, denoted by a class reference followed by a renderer
    registered_renderers = {}
    screen = None

    def __init__(self):
        global screen_size
        display_info = pygame.display.Info()
        screen_size = (display_info.current_w // 2, display_info.current_h // 2)
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

    @staticmethod
    def get_screen_size():
        global screen_size
        return screen_size

    def render_game(self):
        """
        Renders everything in the game
        """
        self.render_background()
        self.render_world_objects()
        self.render_entities()
        self.render_status_text()
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
    def render_status_text():
        global screen_size
        from level import Level
        player = get_player()
        font = pygame.font.SysFont(None, 20)
        health = font.render("Health: {0}".format(player.current_health), True, (255, 0, 0))
        level = font.render("Difficulty: {0}".format(Level.current_level), True, (0, 125, 245))
        score = font.render("Score: {0}".format(player.score), True, (0, 255, 0))
        RendererManager.screen.blit(health, (20, screen_size[1] - 20))
        RendererManager.screen.blit(level, (health.get_width() + 40, screen_size[1] - 20))
        RendererManager.screen.blit(score, (level.get_width() + health.get_width() + 60, screen_size[1] - 20))
