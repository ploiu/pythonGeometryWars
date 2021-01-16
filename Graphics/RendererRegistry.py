from Graphics import RendererManager, PlayerRenderer, TriangleRenderer, PlayerBulletRenderer, SquareRenderer, \
    EnemyBulletRenderer, CircleRenderer, HealthPowerupEntityRenderer, BigPlayerBulletRenderer
from Graphics.BigPlayerBulletPowerupEntityRenderer import BigPlayerBulletPowerupEntityRenderer
from world import Player
from world.entity.bullet import PlayerBullet, EnemyBullet, BigPlayerBullet
from world.entity.enemy import Triangle, Square, Circle
from world.entity.powerup import HealthPowerupEntity, BigPlayerBulletPowerupEntity


def register_renderers():
    RendererManager.register_renderer(Player, PlayerRenderer())
    # enemies
    RendererManager.register_renderer(Triangle, TriangleRenderer())
    RendererManager.register_renderer(Square, SquareRenderer())
    RendererManager.register_renderer(Circle, CircleRenderer())
    # bullets
    RendererManager.register_renderer(PlayerBullet, PlayerBulletRenderer())
    RendererManager.register_renderer(EnemyBullet, EnemyBulletRenderer())
    RendererManager.register_renderer(BigPlayerBullet, BigPlayerBulletRenderer())
    # powerups
    RendererManager.register_renderer(HealthPowerupEntity, HealthPowerupEntityRenderer())
    RendererManager.register_renderer(BigPlayerBulletPowerupEntity, BigPlayerBulletPowerupEntityRenderer())
