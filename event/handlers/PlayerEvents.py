from core import get_player
from event import POWERUP_PICKUP_EVENT


def on_powerup_pickup(event):
    powerup_class = event.__dict__['powerup']
    player = get_player()
    # if either of the player's powerup slots are empty, set the powerup to the first empty slot
    if player.powerups[0] is None:
        player.powerups[0] = powerup_class(player)
    elif player.powerups[1] is None:
        player.powerups[1] = powerup_class(player)


handlers = {
    POWERUP_PICKUP_EVENT: [on_powerup_pickup]
}
