from Graphics import Renderer, RendererManager
from world.entity.enemy import Square
from pygame import draw, Rect


class SquareRenderer(Renderer):
    def __init__(self):
        super(SquareRenderer, self).__init__(Square)

    def render(self, square):
        super(SquareRenderer, self).render(square)
        if square.rect is not None:
            # clear the square's last location
            old_rect = Rect(square.last_x, square.last_y, square.width, square.height)
            draw.rect(RendererManager.screen, (0, 0, 0), old_rect)
            color = (255, 215, 0) if square.is_gold else (0, 255, 0)
            draw.rect(RendererManager.screen, color, square.rect)
            if square.is_dead:
                draw.rect(RendererManager.screen, (0, 0, 0), square.rect)
