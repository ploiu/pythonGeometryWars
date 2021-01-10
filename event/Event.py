from pygame import event

# entity events
ENTITY_UPDATE_EVENT = event.custom_type()
ENTITY_HURT_EVENT = event.custom_type()
PLAYER_DEATH_EVENT = event.custom_type()
SHOOT_EVENT = event.custom_type()
ENEMY_DEATH_EVENT = event.custom_type()

# specifically for level-related use
LEVEL_START_EVENT = event.custom_type()
LEVEL_PROGRESS_EVENT = event.custom_type()
LEVEL_END_EVENT = event.custom_type()
ENEMY_SPAWN_EVENT = event.custom_type()

# specifically for powerups
POWERUP_PICKUP_EVENT = event.custom_type()
POWERUP_USE_EVENT = event.custom_type()
