from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.enemy import Triangle


class TriangleRenderer(Renderer):
    def __init__(self):
        super(TriangleRenderer, self).__init__(Triangle)

    def render(self, triangle):
        super(TriangleRenderer, self).render(triangle)
        # draw a triangle within the rect of the entity
        rect = triangle.rect
        if rect is not None:
            triangle_bottom_left = rect.bottomleft
            triangle_top = rect.midtop
            triangle_bottom_right = rect.bottomright
            color = (255, 215, 0) if triangle.is_gold else (255, 103, 25)
            draw.polygon(RendererManager.screen, color, [triangle_bottom_left, triangle_top, triangle_bottom_right])
