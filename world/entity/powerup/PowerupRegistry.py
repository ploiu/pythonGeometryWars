from random import randint

registered_powerups = []


def register_powerup(powerup_class):
    registered_powerups.append(powerup_class)


def get_random_powerup():
    return registered_powerups[randint(0, len(registered_powerups) - 1)]
