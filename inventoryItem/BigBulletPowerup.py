from inventoryItem.Powerup import Powerup
from world.entity.bullet import PlayerBullet, BigPlayerBullet


class BigBulletPowerup(Powerup):
    def __init__(self, player, life_in_seconds=10):
        super(BigBulletPowerup, self).__init__(player, life_in_seconds)

    def apply_effect(self):
        self.player.bullet_class = BigPlayerBullet
        self.player.shoot_cooldown = 15

    def tick(self):
        self.life_in_ticks -= 1
        if self.life_in_ticks <= 0:
            self.player.bullet_class = PlayerBullet
            self.player.shoot_cooldown = 6

    @property
    def inventory_icon(self):
        from Graphics import get_image
        return get_image("big_bullet_powerup")
