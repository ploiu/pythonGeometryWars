from abc import ABC
import pygame
from pygame.event import Event

from event import ENTITY_UPDATE_EVENT


def update_entities():
    for entity in EntityManager.entities:
        entity.update()
    # now remove all dead entities
    EntityManager.entities = list(filter(lambda it: not it.is_dead, EntityManager.entities))
    # post an event to pygame saying that all entities were updated
    pygame.event.post(Event(ENTITY_UPDATE_EVENT))


def add_entity(entity):
    EntityManager.entities.append(entity)


def remove_entity(entity):
    EntityManager.entities.remove(entity)


class EntityManager(ABC):
    entities = []
