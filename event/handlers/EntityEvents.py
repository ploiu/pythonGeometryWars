import pygame

from core import get_current_level, set_running_game_loop, get_player
from event.Event import ENTITY_HURT_EVENT, PLAYER_DEATH_EVENT, ENEMY_SPAWN_EVENT, SHOOT_EVENT, ENEMY_DEATH_EVENT
from world import add_entity
from world.entity.bullet import PlayerBullet
from world.entity.enemy.BaseEnemy import BaseEnemy


def entity_hurt(hurt_event):
    hurt_entity = hurt_event.__dict__['hurt_entity']
    attacking_entity = hurt_event.__dict__['attacking_entity']
    hurt_entity.current_health -= int(hurt_event.__dict__['damage'])
    if hurt_entity.current_health <= 0 and isinstance(hurt_entity, BaseEnemy):
        pygame.event.post(pygame.event.Event(ENEMY_DEATH_EVENT))
        # if the attacking entity is a player, update that player's score
        if isinstance(attacking_entity, PlayerBullet):
            get_player().score += hurt_entity.score


def player_death(player_death_event):
    player = player_death_event.__dict__['player']
    player.is_dead = True
    set_running_game_loop(False)

def enemy_spawn_event(spawn_event):
    enemy_class = spawn_event.__dict__['enemy_class']
    x = spawn_event.__dict__['x']
    y = spawn_event.__dict__['y']
    enemy = enemy_class()
    enemy.pos_x = x
    enemy.pos_y = y
    add_entity(enemy)


def on_shoot(shoot_event):
    event_info = shoot_event.__dict__
    damage = int(event_info['damage']) if 'damage' in event_info else 5
    angle = int(event_info['angle']) if 'angle' in event_info else 0
    bullet_class = event_info['bullet_class']
    owner = event_info['owner'] if 'owner' in event_info else None
    bullet = bullet_class(damage=damage)
    bullet.owner = owner
    add_entity(bullet)
    bullet.shoot(angle)


def on_entity_death(event):
    # update the difficulty and spawn in an enemy to replace it
    level = get_current_level()
    level.progress(True)


# export this list to register them all
handlers = {
    ENTITY_HURT_EVENT: [entity_hurt],
    PLAYER_DEATH_EVENT: [player_death],
    ENEMY_SPAWN_EVENT: [enemy_spawn_event],
    SHOOT_EVENT: [on_shoot],
    ENEMY_DEATH_EVENT: [on_entity_death]
}
