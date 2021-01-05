from world.Entity import Entity


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(width=10, height=10, max_health=100, armor=0)
        self.ammo_count = 0

    def update(self):
        if self.current_health <= 0:
            self.is_dead = True
            # TODO do something when the player specifically dies

        super(Player, self).update()
