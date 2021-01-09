from Graphics import Renderer, RendererManager
from world.entity.enemy import Square
from pygame import draw


class SquareRenderer(Renderer):
    def __init__(self):
        super(SquareRenderer, self).__init__(Square)

    def render(self, square):
        super(SquareRenderer, self).render(square)
        if square.rect is not None:
            draw.rect(RendererManager.screen, (0, 255, 0), square.rect)
