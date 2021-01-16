from world.entity.bullet.BaseBullet import BaseBullet


class PlayerBullet(BaseBullet):
    def __init__(self, owner):
        super(PlayerBullet, self).__init__(owner=owner)

    def update(self):
        super(PlayerBullet, self).update()

    def check_hit(self):
        from world.entity.powerup import BasePowerupEntity
        from world import Player
        from world.entity import EntityManager
        # get all entities in the world, and check if we intersect with one
        all_entities = EntityManager.entities
        non_owner_entities = list(
            filter(lambda it: it != self.owner and it != self and not isinstance(it, BasePowerupEntity), all_entities))
        # return the first entity this bullet intersects with
        for entity in non_owner_entities:
            if entity.rect is not None and not isinstance(entity, Player) and self.rect.colliderect(entity.rect):
                return entity
