from Graphics import Renderer, RendererManager
from world.entity.powerup import BigPlayerBulletPowerupEntity


class BigPlayerBulletPowerupEntityRenderer(Renderer):
    def __init__(self):
        super(BigPlayerBulletPowerupEntityRenderer, self).__init__(BigPlayerBulletPowerupEntity)

    def render(self, powerup):
        from Graphics import get_image
        super(BigPlayerBulletPowerupEntityRenderer, self).render(powerup)
        # the loaded image to blit to the screen
        if powerup.rect is not None:
            image = get_image("big_bullet_powerup")
            RendererManager.screen.blit(image, powerup.rect)
