import pygame

from core import get_current_level, set_running_game_loop, get_player, get_player_count
from event.Event import ENTITY_HURT_EVENT, PLAYER_DEATH_EVENT, ENEMY_SPAWN_EVENT, SHOOT_EVENT, ENEMY_DEATH_EVENT
from world import add_entity
from world.entity.bullet import PlayerBullet
from world.entity.enemy.BaseEnemy import BaseEnemy
from random import randint


def entity_hurt(hurt_event):
    hurt_entity = hurt_event.__dict__['hurt_entity']
    attacking_entity = hurt_event.__dict__['attacking_entity']
    hurt_entity.current_health -= int(hurt_event.__dict__['damage'])
    if hurt_entity.current_health <= 0 and isinstance(hurt_entity, BaseEnemy):
        pygame.event.post(pygame.event.Event(ENEMY_DEATH_EVENT, {'entity': hurt_entity}))
        # if the attacking entity is a player, update that player's score
        if isinstance(attacking_entity, PlayerBullet):
            attacking_entity.owner.score += hurt_entity.score


def player_death(player_death_event):
    player = player_death_event.__dict__['player']
    player.is_dead = True
    # if all players are dead, kill the game loop
    all_players_dead = True
    for player_index in range(get_player_count()):
        all_players_dead = all_players_dead and get_player(player_index).is_dead

    if all_players_dead:
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
    from world.entity.powerup import get_random_powerup
    # update the difficulty and spawn in an enemy to replace it
    level = get_current_level()
    level.progress(True)
    # get a random power up and spawn it at the entity's location
    entity = event.__dict__['entity']
    if isinstance(entity, BaseEnemy) and entity.is_gold or randint(0, 50) == 1:
        powerup_class = get_random_powerup()
        x, y = entity.pos_x, entity.pos_y
        powerup_entity = powerup_class(pos_x=x, pos_y=y)
        add_entity(powerup_entity)


# export this list to register them all
handlers = {
    ENTITY_HURT_EVENT: [entity_hurt],
    PLAYER_DEATH_EVENT: [player_death],
    ENEMY_SPAWN_EVENT: [enemy_spawn_event],
    SHOOT_EVENT: [on_shoot],
    ENEMY_DEATH_EVENT: [on_entity_death]
}
