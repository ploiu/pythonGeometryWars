import pygame

from Graphics import RendererManager, get_image


class PlayerInventoryRenderer:
    def __init__(self, player_index=0):
        self.player_index = player_index

    def render(self):
        from core import get_player
        screen = RendererManager.screen
        screen_size = RendererManager.get_screen_size()
        # get the top section of the screen to render the player's inventory stuff
        starting_x = screen_size[0] // 2 * 1.5 * self.player_index + 50
        starting_y = 50
        width = screen_size[0] // 2 - 100
        player = get_player(self.player_index)
        left_bumper_image, right_bumper_image = get_image("bumper_left"), get_image("bumper_right")
        # draw the bumpers at the top of the screen, and the corresponding powerups below them
        screen.blit(left_bumper_image, (starting_x + 10, starting_y))
        screen.blit(right_bumper_image, (starting_x + 64, starting_y))
        # draw the powerups
        for (index, powerup) in enumerate(player.powerups):
            if powerup is not None:
                screen.blit(powerup.inventory_icon, (starting_x + 10 + index * 64, starting_y + 40))

        self.draw_box(screen, starting_x, starting_y, 112, 64)

    def draw_box(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, width, height), 1)
