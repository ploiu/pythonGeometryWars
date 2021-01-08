from world.entity.bullet.BaseBullet import BaseBullet


class PlayerBullet(BaseBullet):
    def __init__(self, owner):
        super(PlayerBullet, self).__init__(owner=owner)

    def update(self):
        super(PlayerBullet, self).update()
