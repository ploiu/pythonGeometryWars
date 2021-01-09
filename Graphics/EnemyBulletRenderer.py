from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.bullet import EnemyBullet


class EnemyBulletRenderer(Renderer):
    def __init__(self):
        super(EnemyBulletRenderer, self).__init__(EnemyBullet)

    def render(self, bullet):
        super(EnemyBulletRenderer, self).render(bullet)
        # draw a rectangle where the bullet is
        screen = RendererManager.screen
        draw.rect(screen, (255, 255, 255), bullet.rect)
