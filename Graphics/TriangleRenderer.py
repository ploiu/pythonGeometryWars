from pygame import draw

from Graphics import Renderer, RendererManager
from world.entity.enemy import Triangle


class TriangleRenderer(Renderer):
    def __init__(self):
        super(TriangleRenderer, self).__init__(Triangle)

    def render(self, triangle_entity):
        super(TriangleRenderer, self).render(triangle_entity)
        # draw a triangle within the rect of the entity
        rect = triangle_entity.rect
        triangle_bottom_left = rect.bottomleft
        triangle_top = rect.midtop
        triangle_bottom_right = rect.bottomright
        color = 65, 127, 0
        draw.polygon(RendererManager.screen, color, [triangle_bottom_left, triangle_top, triangle_bottom_right])
