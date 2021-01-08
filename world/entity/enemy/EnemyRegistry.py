"""
A file used to register enemies along with their difficulty, used to make levels scale dynamically
"""
from world.entity.enemy.BaseEnemy import BaseEnemy

registry = {}
"""
values are the difficulty, key is the class of the enemy. Value must be at least 1. a higher value = higher general strength of the enemy
"""


def register_enemy(enemy_class, difficulty):
    # make sure the enemy_class subclasses BaseEnemy
    if not issubclass(enemy_class, BaseEnemy):
        raise ValueError("[{0}] does not subclass BaseEnemy!".format(enemy_class))
    else:
        registry[enemy_class] = max(1, difficulty)


def get_enemies_with_difficulty(difficulty):
    enemies = []
    for (key, value) in registry:
        if value == difficulty:
            enemies.append(key)
    return enemies
