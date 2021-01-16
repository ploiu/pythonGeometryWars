from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.bullet import BigPlayerBullet


class BigPlayerBulletRenderer(Renderer):
    def __init__(self, _type=None):
        super(BigPlayerBulletRenderer, self).__init__(BigPlayerBullet)

    def render(self, bullet):
        super(BigPlayerBulletRenderer, self).render(bullet)
        # draw a rectangle where the bullet is
        screen = RendererManager.screen
        draw.rect(screen, bullet.color, bullet.rect)
