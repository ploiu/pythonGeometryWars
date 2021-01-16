from pygame import draw, Rect

from Graphics import Renderer, RendererManager
from world.entity.bullet import PlayerBullet


class PlayerBulletRenderer(Renderer):
    def __init__(self):
        super(PlayerBulletRenderer, self).__init__(PlayerBullet)

    def render(self, bullet):
        super(PlayerBulletRenderer, self).render(bullet)
        screen = RendererManager.screen
        if (bullet.speed >= bullet.rect.top or bullet.rect.bottom + bullet.speed >=
            RendererManager.get_screen_size()[1]) or (
                bullet.speed >= bullet.rect.left or bullet.rect.right + bullet.speed >=
                RendererManager.get_screen_size()[0]) or bullet.is_dead:
            draw.rect(screen, (0, 0, 0), Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height))
        else:
            # blit out where the bullet was
            draw.rect(screen, (0, 0, 0), Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height))
            # draw a rectangle where the bullet is
            draw.rect(screen, (255, 255, 255), bullet.rect)
