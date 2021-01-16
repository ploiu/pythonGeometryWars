import pygame

from Graphics.Renderer import Renderer
from Graphics.RendererManager import RendererManager
from world import Player


class PlayerRenderer(Renderer):
    def __init__(self):
        super(PlayerRenderer, self).__init__(Player)

    def render(self, player):
        super(PlayerRenderer, self).render(player)
        color = (255, 0, 0) if player.player_number == 0 else (0, 0, 255)
        pygame.draw.rect(RendererManager.screen, color, player.rect)
