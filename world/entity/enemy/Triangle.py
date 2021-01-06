from core import get_player
from world.entity.enemy.BaseEnemy import BaseEnemy


class Triangle(BaseEnemy):
    def __init__(self):
        super(Triangle, self).__init__(width=10, height=10, max_health=3, armor=0, speed=3)
        self.target = None

    def ai(self):
        # attempt to move towards the player
        self.target = get_player()
        target_location = self.target.rect

    def shoot(self, angle):
        pass
