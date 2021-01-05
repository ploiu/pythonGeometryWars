from Graphics import Renderer, RendererManager
from world import Player
import pygame


class PlayerRenderer(Renderer):
    def __init__(self):
        super(PlayerRenderer, self).__init__(Player)

    def render(self, player):
        super(PlayerRenderer, self).render(player)
        color = 255, 0, 0
        pygame.draw.rect(RendererManager.screen, color, player.rect)
