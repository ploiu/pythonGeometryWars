from pygame import event
from pygame.rect import Rect

from core import screen_size
from event import ENTITY_HURT_EVENT
from world import add_entity, EntityManager
from world.entity.Entity import Entity


class BaseBullet(Entity):
    def __init__(self, width=4, height=4, speed=5, damage=5, owner=None):
        super(BaseBullet, self).__init__(width=width, height=height, max_health=1, speed=speed)
        self.damage = damage
        self.owner = owner
        add_entity(self)
        # 8 different angles to shoot in
        self.angle_dict = {
            0: (self.speed, 0),
            45: (self.speed, -self.speed),
            90: (0, -self.speed),
            135: (-self.speed, -self.speed),
            180: (-self.speed, 0),
            225: (-self.speed, self.speed),
            270: (0, self.speed),
            315: (self.speed, self.speed)
        }

    def shoot(self, angle):
        # create our hit box
        self.rect = Rect(self.owner.rect.midtop[0], self.owner.rect.midtop[1], self.width, self.height)
        # update our position to match our hitbox's position
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        # set our speed based on the angle we were shot in
        self.speed_x, self.speed_y = self.angle_dict[angle]

    def update(self):
        super(BaseBullet, self).update()
        # kill the bullet if it's out of bounds
        if 0 > self.rect.top or self.rect.bottom > screen_size[1]:
            self.is_dead = True

        if 0 > self.rect.left or self.rect.right > screen_size[0]:
            self.is_dead = True

        # get any entities this bullet has hit
        hit_entity = self.check_hit()
        if hit_entity is not None:
            self.on_hit(hit_entity)

    def on_hit(self, other):
        # hurt the entity we hit
        event.post(
            event.Event(ENTITY_HURT_EVENT, {'hurt_entity': other, 'attacking_entity': self, 'damage': self.damage}))
        self.is_dead = True

    def check_hit(self):
        # get all entities in the world, and check if we intersect with one
        all_entities = EntityManager.entities
        non_owner_entities = list(filter(lambda it: it != self.owner and it != self, all_entities))
        # return the first entity this bullet intersects with
        for entity in non_owner_entities:
            if entity.rect is not None and self.rect.colliderect(entity.rect):
                return entity
