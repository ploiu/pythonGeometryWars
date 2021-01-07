from world.entity.Entity import Entity


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(width=10, height=10, max_health=100, armor=0, speed=2.5, pos_x=250, pos_y=250)
        self.ammo_count = 0
        self.aim_direction_degrees = 0

    def update(self):
        super(Player, self).update()
