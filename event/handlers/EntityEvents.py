import pygame

from Graphics import RendererManager
from event.Event import ENTITY_HURT_EVENT, PLAYER_DEATH_EVENT, ENEMY_SPAWN_EVENT
from world import add_entity


def entity_hurt(hurt_event):
    hurt_entity = hurt_event.__dict__['hurt_entity']
    attacking_entity = hurt_event.__dict__['attacking_entity']
    hurt_entity.current_health -= int(hurt_event.__dict__['damage'])
    print('PAIN PEKO')


def player_death(player_death_event):
    player = player_death_event.__dict__['player']
    player.is_dead = True
    font = pygame.font.SysFont(None, 24)
    img = font.render('hello', True, (255, 255, 255))
    RendererManager.screen.blit(img, (20, 20))


def enemy_spawn_event(spawn_event):
    enemy_class = spawn_event.__dict__['enemy_class']
    x = spawn_event.__dict__['x']
    y = spawn_event.__dict__['y']
    enemy = enemy_class()
    enemy.pos_x = x
    enemy.pos_y = y
    add_entity(enemy)


# export this list to register them all
handlers = {
    ENTITY_HURT_EVENT: [entity_hurt],
    PLAYER_DEATH_EVENT: [player_death],
    ENEMY_SPAWN_EVENT: [enemy_spawn_event]
}
