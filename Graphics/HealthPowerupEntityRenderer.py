from Graphics import Renderer, RendererManager
from world.entity.powerup import HealthPowerupEntity


class HealthPowerupEntityRenderer(Renderer):
    def __init__(self):
        super(HealthPowerupEntityRenderer, self).__init__(HealthPowerupEntity)

    def render(self, powerup):
        from Graphics import get_image
        super(HealthPowerupEntityRenderer, self).render(powerup)
        # the loaded image to blit to the screen
        if powerup.rect is not None:
            image = get_image("health_powerup")
            RendererManager.screen.blit(image, powerup.rect)
