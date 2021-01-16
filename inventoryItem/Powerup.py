from abc import ABC, abstractmethod

from core import desired_fps


class Powerup(ABC):
    """
    Represents a powerup in the player's inventory
    """

    def __init__(self, player, life_in_seconds=60):
        self.player = player
        self.life_in_ticks = life_in_seconds * 1_000 * desired_fps

    @abstractmethod
    def apply_effect(self):
        pass

    def tick(self):
        """
        Used to update the powerup state on each tick. Not necessary to override unless needed
        :return: None
        """
        pass

    @property
    @abstractmethod
    def inventory_icon(self):
        """
        Used to get the icon for this powerup so that we don't have to do anything hacky with entities and renderers
        :return: the registered image used with this powerup
        """
        return None
