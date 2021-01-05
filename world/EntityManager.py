from abc import ABC


def update_entities():
    for entity in EntityManager.entities:
        entity.update()

    # now remove all dead entities
    EntityManager.entities = list(filter(lambda it: not it.is_dead, EntityManager.entities))


def add_entity(entity):
    EntityManager.entities.append(entity)


def remove_entity(entity):
    EntityManager.entities.remove(entity)


class EntityManager(ABC):
    entities = []
