import pygame

# the screen background color
from core import get_player, get_player_count
from world import EntityManager

screen_background = 0, 0, 0
screen_size = None


class RendererManager:
    # the list of all renderers in the game, denoted by a class reference followed by a renderer
    registered_renderers = {}
    screen = None
    font = None

    def __init__(self):
        global screen_size
        from Graphics.PlayerInventoryRenderer import PlayerInventoryRenderer
        self.player_inventory_renderers = [PlayerInventoryRenderer(player_index) for player_index in
                                           range(get_player_count())]
        RendererManager.font = pygame.font.SysFont(None, 20)
        display_info = pygame.display.Info()
        if display_info.current_w < 1000 or display_info.current_h < 500:
            screen_size = display_info.current_w, display_info.current_h
            RendererManager.screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        else:
            screen_size = (display_info.current_w // 2, display_info.current_h // 2)
            RendererManager.screen = pygame.display.set_mode(screen_size)

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
        # self.render_background()
        self.render_world_objects()
        self.render_entities()
        self.render_status_text()
        # render player inventories
        for renderer in self.player_inventory_renderers:
            renderer.render()
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
        # clear out the entire bottom section
        clear_rect = pygame.Rect(0, screen_size[1] - 20, screen_size[0], 20)
        pygame.draw.rect(RendererManager.screen, (0, 0, 0), clear_rect)
        for player_number in range(get_player_count()):
            # get the top section of the screen to render the player's inventory stuff
            starting_x = screen_size[0] // 2 * player_number + 50
            starting_y = screen_size[1] - 20
            player = get_player(player_number)
            health = RendererManager.font.render("Health: {0}".format(player.current_health), True, (255, 0, 0))
            level = RendererManager.font.render("Difficulty: {0}".format(Level.current_level), True, (0, 125, 245))
            score = RendererManager.font.render("Score: {0}".format(player.score), True, (0, 255, 0))
            RendererManager.blit_text_area(health, (starting_x + 20, starting_y))
            RendererManager.blit_text_area(level, (starting_x + 20 + health.get_width() + 40, starting_y))
            RendererManager.blit_text_area(score,
                                           (starting_x + 20 + level.get_width() + health.get_width() + 60, starting_y))

    @staticmethod
    def blit_text_area(surface, coords):
        RendererManager.screen.blit(surface, coords)
