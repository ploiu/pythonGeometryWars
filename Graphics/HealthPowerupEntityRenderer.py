from Graphics import Renderer, RendererManager
from world.entity.powerup import HealthPowerupEntity
from pygame import draw, Rect


class HealthPowerupEntityRenderer(Renderer):
    def __init__(self):
        super(HealthPowerupEntityRenderer, self).__init__(HealthPowerupEntity)

    def render(self, powerup):
        from Graphics import get_image
        super(HealthPowerupEntityRenderer, self).render(powerup)
        image = get_image("health_powerup")

        # the loaded image to blit to the screen
        if powerup.rect is not None:
            RendererManager.screen.blit(image, powerup.rect)

        if powerup.is_dead:
            rect = Rect(powerup.pos_x, powerup.pos_y, image.get_width(), image.get_height())
            draw.rect(RendererManager.screen, (0, 0, 0), rect)
