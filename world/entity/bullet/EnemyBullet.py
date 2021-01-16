from core import get_player, get_player_count
from world.entity.bullet.BaseBullet import BaseBullet


class EnemyBullet(BaseBullet):
    def __init__(self, damage=5):
        super(EnemyBullet, self).__init__(damage=damage)

    def check_hit(self):
        first_player = get_player(0)
        second_player = get_player(1) if get_player_count() == 2 else None
        if first_player.rect.colliderect(self.rect):
            return first_player
        elif second_player is not None and second_player.rect.colliderect(self.rect):
            return second_player
        else:
            return None
