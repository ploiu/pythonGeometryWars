from core import get_player
from world.entity.bullet.BaseBullet import BaseBullet


class EnemyBullet(BaseBullet):
    def __init__(self, damage=5):
        super(EnemyBullet, self).__init__(damage=damage)

    def check_hit(self):
        return get_player() if get_player().rect.colliderect(self.rect) else None
