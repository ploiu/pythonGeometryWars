from inventoryItem import HealthPowerup
from world.entity.powerup.BasePowerupEntity import BasePowerupEntity


class HealthPowerupEntity(BasePowerupEntity):
    def __init__(self, pos_x=0, pos_y=0):
        super(HealthPowerupEntity, self).__init__(pos_x=pos_x, pos_y=pos_y, powerup_type=HealthPowerup)
