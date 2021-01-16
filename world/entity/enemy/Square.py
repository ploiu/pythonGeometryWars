from random import randint

from pygame import event

import Graphics
from core import desired_fps, difficulty_modifier, shoot_angles
from event import SHOOT_EVENT
from world.entity.bullet.EnemyBullet import EnemyBullet
from world.entity.enemy.BaseEnemy import BaseEnemy


class Square(BaseEnemy):
    def __init__(self):
        super(Square, self).__init__(width=10, height=10, max_health=5, armor=0, speed=1, score=100)
        # the amount of ticks since we last shot something
        self.ticks_since_last_shoot = randint(0, 5000)
        self.shoot_interval = (5_000 // desired_fps // difficulty_modifier // (10 if self.is_gold else 1))
        self.change_direction_interval = 10_000 // desired_fps
        self.ticks_since_direction_changed = randint(0, 10_000)

    def ai(self):
        self.ticks_since_last_shoot += 1
        if self.ticks_since_last_shoot >= self.shoot_interval:
            self.ticks_since_last_shoot = 0
            # shoot a bullet
            angle_index = randint(0, len(shoot_angles) - 1)
            self.shoot(shoot_angles[angle_index])
        # handle direction change
        self.ticks_since_direction_changed += 1
        if self.ticks_since_direction_changed >= self.change_direction_interval:
            self.ticks_since_direction_changed = 0
            multipliers = [1, -1]
            self.speed_x = self.speed * multipliers[randint(0, 1)]
            self.speed_y = self.speed * multipliers[randint(0, 1)]
        # change direction if past the edges of the screen
        if self.pos_x <= 0:
            self.speed_x = self.speed
        elif self.pos_x >= Graphics.RendererManager.get_screen_size()[0]:
            self.speed_x = -self.speed

        if self.pos_y <= 0:
            self.speed_y = self.speed
        elif self.pos_y >= Graphics.RendererManager.get_screen_size()[1]:
            self.speed_y = -self.speed
            
        self.is_dirty = True

    def update(self):
        super(Square, self).update()

    def shoot(self, angle):
        event_info = {
            'damage': self.strength,
            'angle': angle,
            'bullet_class': EnemyBullet,
            'owner': self
        }
        event.post(event.Event(SHOOT_EVENT, event_info))
