from world.entity.Entity import Entity
from abc import ABC, abstractmethod


class BaseEnemy(Entity):
    def __init__(self, width, height, max_health, armor, speed):
        super(BaseEnemy, self).__init__(width=width, height=height, max_health=max_health, armor=armor, speed=speed)

    @abstractmethod
    def ai(self):
        """
        Details the steps that this enemy takes to harm and kill the player
        :return: None
        """
        pass

    def update(self):
        super(BaseEnemy, self).update()
        self.ai()

    @abstractmethod
    def shoot(self, angle):
        pass
