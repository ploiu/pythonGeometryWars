from core import desired_fps, difficulty_modifier, get_player, get_player_count
from event import ENTITY_HURT_EVENT
from world.entity.enemy.BaseEnemy import BaseEnemy
from random import randint
from pygame import event


class Circle(BaseEnemy):
    def __init__(self):
        super(Circle, self).__init__(width=10, height=10, max_health=4, armor=0, speed=2, score=100, strength=3)
        # the amount of time it takes to check for player location
        self.check_interval = 3_000 // desired_fps // difficulty_modifier
        self.last_check = randint(0, 3_000)
        # the index of the target player
        self.target_player_index = randint(0, get_player_count() - 1)

    def ai(self):
        self.last_check += 1
        if self.last_check >= self.check_interval:
            self.last_check = 0
            velocity_modifier = self.get_velocity_to_target(get_player(self.target_player_index).rect)
            self.speed_x = self.speed * velocity_modifier[0]
            self.speed_y = self.speed * velocity_modifier[1]
        else:
            pass  # Todo shoot
        # if the circle is inside the player, kill the circle and damage the player
        if self.rect.colliderect(get_player(self.target_player_index).rect):
            event.post(
                event.Event(ENTITY_HURT_EVENT,
                            {
                                'hurt_entity': get_player(self.target_player_index),
                                'attacking_entity': self,
                                'damage': self.strength
                            }
                            )
            )
            self.is_dead = True

    def update(self):
        super(Circle, self).update()

    def shoot(self, angle):
        pass
