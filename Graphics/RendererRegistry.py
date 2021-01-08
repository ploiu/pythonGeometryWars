from Graphics import RendererManager, PlayerRenderer, TriangleRenderer, PlayerBulletRenderer
from world import Player
from world.entity.bullet import PlayerBullet
from world.entity.enemy import Triangle


def register_renderers():
    RendererManager.register_renderer(Player, PlayerRenderer())
    RendererManager.register_renderer(Triangle, TriangleRenderer())
    RendererManager.register_renderer(PlayerBullet, PlayerBulletRenderer())
