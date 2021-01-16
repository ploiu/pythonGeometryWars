from pygame import draw, Rect

from Graphics import Renderer, RendererManager
from world.entity.bullet import BigPlayerBullet


class BigPlayerBulletRenderer(Renderer):
    def __init__(self, _type=None):
        super(BigPlayerBulletRenderer, self).__init__(BigPlayerBullet)

    def render(self, bullet):
        super(BigPlayerBulletRenderer, self).render(bullet)
        screen = RendererManager.screen
        if (bullet.speed >= bullet.rect.top or bullet.rect.bottom + bullet.speed >=
            RendererManager.get_screen_size()[1]) or (
                bullet.speed >= bullet.rect.left or bullet.rect.right + bullet.speed >=
                RendererManager.get_screen_size()[0]) or bullet.is_dead:
            draw.rect(screen, (0, 0, 0), Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height))
        else:
            # wipe out where the bullet used to be
            old_rect = Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height)
            draw.rect(screen, (0, 0, 0), old_rect)
            # draw a rectangle where the bullet is
            draw.rect(screen, bullet.color, bullet.rect)
