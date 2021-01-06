from Graphics import RendererManager, PlayerRenderer, TriangleRenderer
from world import Player
from world.entity.enemy import Triangle


def register_renderers():
    RendererManager.register_renderer(Player, PlayerRenderer())
    RendererManager.register_renderer(Triangle, TriangleRenderer())
