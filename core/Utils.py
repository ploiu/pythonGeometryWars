"""
These functions cannot be imported into main, as they require use of the game registry
"""

# used to reference core game objects (and keep them in memory to prevent them from being garbage collected)
game_registry = {}

def get_player():
    return game_registry['player']


def get_current_level():
    return game_registry['current_level'] if 'current_level' in game_registry else None
