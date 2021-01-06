"""
These functions cannot be imported into main, as they require use of the game registry
"""

game_registry = {}

def get_player():
    return game_registry['player']
