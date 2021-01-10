from abc import ABC, abstractmethod

from core import desired_fps, get_player
from event import POWERUP_PICKUP_EVENT
from world.entity.Entity import Entity
import pygame
from pygame import event


class BasePowerupEntity(Entity, ABC):
    def __init__(self, life_in_seconds=10, pos_x=0, pos_y=0, powerup_type=None):
        super(BasePowerupEntity, self).__init__(width=10, height=10, pos_x=pos_x, pos_y=pos_y)
        self.life_in_ticks = life_in_seconds * 1_000 * desired_fps
        self.current_age = 0
        # the associated powerup class that this powerup is tied to
        self.powerup_type = powerup_type

    def update(self):
        self.current_age += 1
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        if self.current_age >= self.life_in_ticks:
            self.is_dead = True
        elif self.check_collide():
            event.post(event.Event(POWERUP_PICKUP_EVENT, {'powerup': self.powerup_type}))
            self.is_dead = True

    def check_collide(self):
        return get_player().rect.colliderect(self.rect)
