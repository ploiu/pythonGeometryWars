import pygame

from core import get_player
from event import ENTITY_HURT_EVENT
from world.entity.enemy.BaseEnemy import BaseEnemy


class Triangle(BaseEnemy):
    def __init__(self):
        super(Triangle, self).__init__(width=10, height=10, max_health=3, armor=0, speed=2.2)
        self.target = None

    def ai(self):
        # attempt to move towards the player
        self.target = get_player()
        target_location = self.target.rect
        if target_location is not None:
            # create the search radius as a rectangle around our hitbox
            search_radius = self.rect.inflate(200, 200)
            search_radius.center = self.rect.center
            if search_radius.contains(target_location):
                self._follow_player()
            else:
                self.speed_x = 0
                self.speed_y = 0
            # now if we are within the player, attack them and kill ourselves
            if self.rect.colliderect(self.target.rect):
                pygame.event.post(pygame.event.Event(ENTITY_HURT_EVENT,
                                                     {'hurt_entity': self.target, 'attacking_entity': self,
                                                      'damage': 10}))
                self.is_dead = True

    def _follow_player(self):
        # get the velocity modifiers for where we need to move
        velocities = super(Triangle, self).get_velocity_to_target(self.target.rect)
        self.speed_x = velocities[0] * self.speed
        self.speed_y = velocities[1] * self.speed

    def shoot(self, angle):
        # triangles don't shoot, they act like suicide bombers
        pass
