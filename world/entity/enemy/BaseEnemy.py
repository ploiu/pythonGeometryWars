from abc import abstractmethod

from world.entity.Entity import Entity


class BaseEnemy(Entity):
    def __init__(self, width, height, max_health, armor, speed, difficulty=0):
        super(BaseEnemy, self).__init__(width=width, height=height, max_health=max_health, armor=armor, speed=speed)
        self.difficulty = max(1, difficulty)  # make sure the difficulty isn't 0

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
