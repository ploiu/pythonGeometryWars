from random import randint

from pygame import event

from Graphics import RendererManager
from core.GlobalValues import difficulty_modifier
from core.Utils import get_player, game_registry, get_player_count
from event import ENEMY_SPAWN_EVENT
from world import EntityManager
from world.entity import get_enemy_count
from world.entity.enemy import enemy_registry


class Level:
    current_level = 1

    def __init__(self):
        # set our difficulty, which equates to the number and type of enemies that can spawn
        self.difficulty = Level.current_level * 10 * difficulty_modifier
        # get entries in the enemy registry to create easy pairs between an enemy and its difficulty
        self.enemy_pool = list(enemy_registry.items())

    def update_difficulty(self, increase):
        Level.current_level += increase
        self.difficulty = Level.current_level * 10 * difficulty_modifier

    def pick_enemy(self):
        potential_enemies = list(filter(lambda it: it[1] <= self.difficulty, self.enemy_pool))
        enemy_index = randint(0, len(potential_enemies) - 1)
        enemy = potential_enemies[enemy_index][0]
        return enemy

    def start(self):
        # pick a random number of enemies to spawn initially
        game_registry['current_level'] = self
        max_enemies_to_spawn = 1
        for index in range(0, max_enemies_to_spawn):
            self.spawn_enemy()

    def progress(self, from_dead_entity=False):
        if not from_dead_entity:
            self.update_difficulty(1)
        # decide if we should spawn a new entity
        all_players_dead = True
        for player_number in range(get_player_count()):
            all_players_dead = all_players_dead and get_player(player_number).is_dead

        if not all_players_dead and get_enemy_count() <= 40:
            if from_dead_entity:
                self.spawn_enemy()
            else:
                # level has progressed, spawn more enemies equal to the current level
                for i in range(0, Level.current_level):
                    self.spawn_enemy()

    def spawn_enemy(self):
        if len(EntityManager.entities) <= 100:
            enemy = self.pick_enemy()
            current_x = randint(10, RendererManager.get_screen_size()[0])
            current_y = randint(10, RendererManager.get_screen_size()[1])
            event_data = {'enemy_class': enemy, 'x': current_x, 'y': current_y}
            event.post(event.Event(ENEMY_SPAWN_EVENT, event_data))
