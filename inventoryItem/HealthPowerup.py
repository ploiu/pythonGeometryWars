from inventoryItem.Powerup import Powerup


class HealthPowerup(Powerup):
    def apply_effect(self):
        self.player.current_health = min(self.player.max_health,
                                         self.player.max_health // 4 + self.player.current_health)

    @property
    def inventory_icon(self):
        from Graphics import get_image
        return get_image("health_powerup")
