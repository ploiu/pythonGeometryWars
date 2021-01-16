from abc import ABC

import pygame
from pygame import event

from core import desired_fps, get_player, get_player_count
from event import POWERUP_PICKUP_EVENT
from world.entity.Entity import Entity


class BasePowerupEntity(Entity, ABC):
    def __init__(self, life_in_seconds=10, pos_x=0, pos_y=0, powerup_type=None):
        """
        Initializes the powerup entity and sets its location in the world. This does not add it to the entity list
        :param life_in_seconds: the amount of seconds this powerup entity can stay on the screen before it is removed
        :param pos_x: the x position for this entity
        :param pos_y: the y position for this entity
        :param powerup_type: the associated Powerup class this entity is associated with. When obtained, this class is 
            used in an event that gets processed by an event handler
        """
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
            event.post(
                event.Event(POWERUP_PICKUP_EVENT, {'powerup': self.powerup_type, 'player': self.get_collided_player()}))
            self.is_dead = True

    def check_collide(self):
        for player_index in range(get_player_count()):
            if get_player(player_index).rect.colliderect(self.rect):
                return True

        return False

    def get_collided_player(self):
        if get_player_count() == 1:
            return get_player(0)
        else:
            first_player, second_player = get_player(0), get_player(1)
            return first_player if first_player.rect.colliderect(self.rect) else second_player
