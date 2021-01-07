from world.WorldObject import WorldObject
from pygame import Rect


class Entity(WorldObject):
    def __init__(self, width=0, height=0, pos_x=0, pos_y=0, max_health=0, armor=0, speed=0):
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
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        if self.current_health <= 0:
            self.is_dead = True
        else:
            # player is not dead, update states
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
        self.rect = Rect(self.pos_x, self.pos_y, self.width, self.height)

    def set_velocity_x(self, velocity):
        self.speed_x = velocity

    def set_velocity_y(self, velocity):
        self.speed_y = velocity

    def get_velocity_to_target(self, target_rect):
        our_x, our_y = self.rect.center
        target_x, target_y = target_rect.center
        velocity_x, velocity_y = 0, 0
        if our_x > target_x:
            velocity_x = -1
        elif our_x < target_x:
            velocity_x = 1
        else:
            velocity_x = 0
        # now determine velocity y
        if our_y > target_y:
            velocity_y = -1
        elif our_y < target_y:
            velocity_y = 1
        else:
            velocity_y = 0
        return velocity_x, velocity_y
