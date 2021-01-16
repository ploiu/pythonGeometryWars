from inventoryItem.BigBulletPowerup import BigBulletPowerup
from world.entity.powerup.BasePowerupEntity import BasePowerupEntity


class BigPlayerBulletPowerupEntity(BasePowerupEntity):
    def __init__(self, pos_x=0, pos_y=0):
        super(BigPlayerBulletPowerupEntity, self).__init__(pos_x=pos_x, pos_y=pos_y, powerup_type=BigBulletPowerup)
