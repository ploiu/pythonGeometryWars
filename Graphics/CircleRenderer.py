from Graphics import Renderer, RendererManager
from world.entity.enemy import Circle
from pygame import draw


class CircleRenderer(Renderer):
    def __init__(self):
        super(CircleRenderer, self).__init__(Circle)

    def render(self, circle):
        super(CircleRenderer, self).render(circle)
        if circle.rect is not None:
            color = (255, 215, 0) if circle.is_gold else (148, 37, 148)
            draw.circle(RendererManager.screen, color, circle.rect.center, circle.rect.width / 2)
