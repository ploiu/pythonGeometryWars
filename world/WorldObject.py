from abc import ABC


class WorldObject(ABC):

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
