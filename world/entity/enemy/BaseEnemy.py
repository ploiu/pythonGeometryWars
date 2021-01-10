from abc import abstractmethod

from core import difficulty_modifier
from world.entity.Entity import Entity
from random import randint


class BaseEnemy(Entity):
    def __init__(self, width, height, max_health, armor, speed, difficulty=0, score=0, strength=5):
        super(BaseEnemy, self).__init__(width=width, height=height, max_health=max_health, armor=armor, speed=speed)
        self.difficulty = max(1, difficulty)  # make sure the difficulty isn't 0
        self.score = score * difficulty_modifier
        self.is_gold = False
        self.strength = strength
        # give a 1/100 chance of becoming uber strong
        if randint(0, 100) == 1:
            self.make_golden()

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

    def make_golden(self):
        self.speed *= 2
        self.score *= 10
        self.max_health *= 2
        self.width *= 2
        self.height *= 2
        self.armor += 3
        self.strength *= 2
        self.is_gold = True
