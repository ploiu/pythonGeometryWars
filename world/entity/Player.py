from event import PLAYER_DEATH_EVENT
from world.entity.Entity import Entity
from pygame import event


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(width=10, height=10, max_health=100, armor=0, speed=2.5, pos_x=250, pos_y=250)
        self.ammo_count = 0
        self.aim_direction_degrees = 0
        self.score = 0
        self.power_ups = []

    def update(self):
        super(Player, self).update()
        if self.current_health <= 0:
            event.post(event.Event(PLAYER_DEATH_EVENT, {'player': self}))
