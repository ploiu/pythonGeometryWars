from Graphics import RendererManager, PlayerRenderer, TriangleRenderer, PlayerBulletRenderer, SquareRenderer, \
    EnemyBulletRenderer, CircleRenderer, HealthPowerupEntityRenderer
from world import Player
from world.entity.bullet import PlayerBullet, EnemyBullet
from world.entity.enemy import Triangle, Square, Circle
from world.entity.powerup import HealthPowerupEntity


def register_renderers():
    RendererManager.register_renderer(Player, PlayerRenderer())
    RendererManager.register_renderer(Triangle, TriangleRenderer())
    RendererManager.register_renderer(Square, SquareRenderer())
    RendererManager.register_renderer(PlayerBullet, PlayerBulletRenderer())
    RendererManager.register_renderer(EnemyBullet, EnemyBulletRenderer())
    RendererManager.register_renderer(Circle, CircleRenderer())
    RendererManager.register_renderer(HealthPowerupEntity, HealthPowerupEntityRenderer())
