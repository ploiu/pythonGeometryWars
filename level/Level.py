from random import randint

from pygame import event

from core import screen_size
from core.GlobalValues import difficulty_modifier
from core.Utils import game_registry, get_player
from event import ENEMY_SPAWN_EVENT, LEVEL_END_EVENT, LEVEL_START_EVENT
from world.entity import get_enemy_count
from world.entity.enemy import enemy_registry


class Level:
    current_level = 1

    def __init__(self, set_enemies=None):
        # set our difficulty, which equates to the number and type of enemies that can spawn
        self.difficulty = (20 * max(Level.current_level, 1)) * difficulty_modifier
        # get entries in the enemy registry to create easy pairs between an enemy and its difficulty
        self.enemy_pool = list(enemy_registry.items())
        if set_enemies is None:
            self.set_enemies = self.pick_enemies_for_level()
        else:
            self.set_enemies = set_enemies

    def pick_enemies_for_level(self):
        difficulty_left = self.difficulty
        enemies = []
        # keep going until difficulty_left is less than zero, and pick enemies from the registered list of enemies
        while difficulty_left >= 0:
            # pick an enemy and subtract its difficulty score from our difficulty_left
            enemy_index = randint(0, len(self.enemy_pool) - 1)
            enemy = self.enemy_pool[enemy_index][0]
            difficulty_left -= self.enemy_pool[enemy_index][1]
            enemies.append(enemy)

        return enemies

    def start(self):
        # pick a random number of enemies to spawn initially
        max_enemies_to_spawn = (len(self.set_enemies) - 1) // 2
        game_registry['current_level'] = self
        for index in range(0, max_enemies_to_spawn):
            self.spawn_enemy(index)

        # now remove those spawned enemies
        for index in range(0, max_enemies_to_spawn):
            del self.set_enemies[0]

    def progress(self):
        # decide if we should spawn a new entity
        if len(self.set_enemies) > 0:
            self.spawn_enemy(0)
            del self.set_enemies[0]
        elif not get_player().is_dead and get_enemy_count() <= 0:
            print('LEVEL CLEAR!')
            # TODO print to the screen that the level cleared
            event.post(event.Event(LEVEL_END_EVENT))
            event.post(event.Event(LEVEL_START_EVENT))

    def spawn_enemy(self, index):
        # TODO improve to prevent from spawning on player, maybe spawn close to out of bounds?
        max_x, max_y = screen_size
        current_x = randint(20, max_x - 20)
        current_y = randint(20, max_y - 20)
        event_data = {'enemy_class': self.set_enemies[index], 'x': current_x, 'y': current_y}
        event.post(event.Event(ENEMY_SPAWN_EVENT, event_data))
