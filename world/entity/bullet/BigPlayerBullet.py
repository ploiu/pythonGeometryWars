from event import ENTITY_HURT_EVENT
from world.entity.bullet import PlayerBullet
from pygame import event
from random import randint


class BigPlayerBullet(PlayerBullet):
    """
    This bullet has a bigger hit box and doesn't die when it hits another enemy
    """

    def __init__(self, owner):
        super(BigPlayerBullet, self).__init__(owner)
        self.width, self.height = 15, 15
        self.damage = 100
        self.color = (255, 144, 99) if randint(0, 1) == 0 else (147, 82, 234)

    def on_hit(self, other):
        # hurt the entity we hit
        event.post(
            event.Event(ENTITY_HURT_EVENT, {'hurt_entity': other, 'attacking_entity': self, 'damage': self.damage}))
