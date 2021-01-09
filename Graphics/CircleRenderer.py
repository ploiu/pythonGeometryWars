from Graphics import Renderer, RendererManager
from world.entity.enemy import Circle
from pygame import draw


class CircleRenderer(Renderer):
    def __init__(self):
        super(CircleRenderer, self).__init__(Circle)

    def render(self, circle):
        super(CircleRenderer, self).render(circle)
        color = 148, 37, 148
        if circle.rect is not None:
            draw.circle(RendererManager.screen, color, circle.rect.center, circle.rect.width / 2)
