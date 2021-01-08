from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.bullet import PlayerBullet


class PlayerBulletRenderer(Renderer):
    def __init__(self):
        super(PlayerBulletRenderer, self).__init__(PlayerBullet)

    def render(self, bullet):
        super(PlayerBulletRenderer, self).render(bullet)
        # draw a rectangle where the bullet is
        screen = RendererManager.screen
        draw.rect(screen, (255, 255, 255), bullet.rect)
