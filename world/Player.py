from world.Entity import Entity


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(width=10, height=10, max_health=100, armor=0, speed=2.5, pos_x=250, pos_y=250)
        self.ammo_count = 0
        self.aim_direction_degrees = 0

    def update(self):
        if self.current_health <= 0:
            self.is_dead = True
            # TODO do something when the player specifically dies
        else:
            # player is not dead, update states
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
        super(Player, self).update()
