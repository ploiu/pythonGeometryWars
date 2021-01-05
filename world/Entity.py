from world.WorldObject import WorldObject
from pygame import Rect


class Entity(WorldObject):
    def __init__(self, width=0, height=0, pos_x=0, pos_y=0, max_health=0, armor=0):
        super(Entity, self).__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_health = max_health
        self.armor = armor
        self.width = width
        self.height = height
        self.rect = None
        self.is_dead = False
        self.current_health = self.max_health

    def update(self):
        self.rect = Rect(self.pos_x, self.pos_y, self.width, self.height)
