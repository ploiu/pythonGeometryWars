from Graphics import Renderer, RendererManager
from world.entity.powerup import BigPlayerBulletPowerupEntity
from pygame import draw, Rect


class BigPlayerBulletPowerupEntityRenderer(Renderer):
    def __init__(self):
        super(BigPlayerBulletPowerupEntityRenderer, self).__init__(BigPlayerBulletPowerupEntity)

    def render(self, powerup):
        from Graphics import get_image
        super(BigPlayerBulletPowerupEntityRenderer, self).render(powerup)
        image = get_image("big_bullet_powerup")

        # the loaded image to blit to the screen
        if powerup.rect is not None:
            RendererManager.screen.blit(image, powerup.rect)

        if powerup.is_dead:
            rect = Rect(powerup.pos_x, powerup.pos_y, image.get_width(), image.get_height())
            draw.rect(RendererManager.screen, (0, 0, 0), rect)
