from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.bullet import EnemyBullet
from pygame import Rect


class EnemyBulletRenderer(Renderer):
    def __init__(self):
        super(EnemyBulletRenderer, self).__init__(EnemyBullet)

    def render(self, bullet):
        screen = RendererManager.screen
        if (bullet.speed >= bullet.rect.top or bullet.rect.bottom + bullet.speed >=
            RendererManager.get_screen_size()[1]) or (
                bullet.speed >= bullet.rect.left or bullet.rect.right + bullet.speed >=
                RendererManager.get_screen_size()[0]):
            draw.rect(screen, (0, 0, 0),
                      Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height).inflate(10, 10))
        else:
            # blit out where the bullet was
            draw.rect(screen, (0, 0, 0),
                      Rect(bullet.last_x, bullet.last_y, bullet.width, bullet.height).inflate(10, 10))
            # draw a rectangle where the bullet is
            draw.rect(screen, (255, 255, 255), bullet.rect)
