from enum import IntEnum


class SNESButtons(IntEnum):
    X = 0
    A = 1
    B = 2
    Y = 3
    L_BUMPER = 4
    R_BUMPER = 5
    SELECT = 8
    START = 9


class SNESAxes(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


# the mappings are different on windows for some reason
class SNESAxes_Win(IntEnum):
    HORIZONTAL = 3
    VERTICAL = 4
