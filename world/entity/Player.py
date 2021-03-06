from event import PLAYER_DEATH_EVENT
from world.entity.Entity import Entity
from pygame import event

from world.entity.bullet import PlayerBullet


class Player(Entity):
    def __init__(self, player_number=0):
        super(Player, self).__init__(width=10, height=10, max_health=100, armor=0, speed=2.5, pos_x=250, pos_y=250)
        self.aim_direction_degrees = 0
        self.score = 0
        # if this is ever above 1, we shoot in the angle it is specified
        self.shooting_angle = -1
        # the number of cooldown frames in between times the player can shoot
        self.shoot_cooldown = 6
        # the number of frames since this player shot a bullet
        self.time_since_last_shoot = 6
        # the list of powerups the player has, length must always be 2
        self.powerups = [None, None]
        # the list of active powerups the player has, length must always be 2
        self.active_powerups = [None, None]
        # if we are player 1 or 2
        self.player_number = player_number
        # the type of bullet the player has
        self.bullet_class = PlayerBullet

    def update(self):
        super(Player, self).update()
        self.time_since_last_shoot += 1
        if self.current_health <= 0:
            event.post(event.Event(PLAYER_DEATH_EVENT, {'player': self}))
        elif self.shooting_angle > -1:
            # if our time since last shoot is at least our cooldown, reset the time and shoot
            if self.time_since_last_shoot >= self.shoot_cooldown:
                self.time_since_last_shoot = 0
                self.shoot(self.shooting_angle)

        if not self.is_dead:
            # for each active powerup, tick it
            for (index, powerup) in enumerate(self.active_powerups):
                if powerup is not None:
                    powerup.tick()
                    if powerup.life_in_ticks <= 0:
                        # remove the powerup from the active powerup list
                        self.active_powerups[index] = None

    def shoot(self, angle):
        self.bullet_class(self).shoot(angle)

    def update_shooting_angle(self, new_angle_amount):
        """
        Updates the angle we are shooting at based on the passed new amount and our current angle
        :param new_angle_amount: the angle to apply to our new
        :return: 
        """
        # use a dict with all the combinations instead of a complex if statement (current angle first, new angle second)
        # TODO this can probably be simplified and optimized
        angle_combos = {
            # we aren't shooting
            (-1, 0): 0,
            (-1, 90): 90,
            (-1, 180): 180,
            (-1, 270): 270,
            # we are shooting and this produces an angle shot
            (0, 90): 45,
            (90, 180): 135,
            (180, 270): 225,
            (0, 270): 315,
            # we are shooting and let go of a button
            (0, -1): -1,
            (45, -1): 90,
            (45, -90): 0,
            (90, -90): -1,
            (135, -90): 180,
            (135, -180): 90,
            (180, -180): -1,
            (225, -180): 270,
            (225, -270): 180,
            (270, -270): -1,
            (315, -1): 270,
            (315, -270): 0
        }
        if new_angle_amount >= 0:
            # if the current combinations is in the angle_combos, we shoot at that angle
            if (self.shooting_angle, new_angle_amount) in angle_combos:
                self.shooting_angle = angle_combos[(self.shooting_angle, new_angle_amount)]
            elif (new_angle_amount, self.shooting_angle) in angle_combos:
                self.shooting_angle = angle_combos[(new_angle_amount, self.shooting_angle)]
            # else if the amount is positive, we set our angle to the new angle amount
            else:
                self.shooting_angle = new_angle_amount
        else:
            # if the current combinations is in the angle_combos, we shoot at that angle
            if (self.shooting_angle, new_angle_amount) in angle_combos:
                self.shooting_angle = angle_combos[(self.shooting_angle, new_angle_amount)]
            elif (new_angle_amount, self.shooting_angle) in angle_combos:
                self.shooting_angle = angle_combos[(new_angle_amount, self.shooting_angle)]
            # else if the amount is positive, we set our angle to -1
            else:
                self.shooting_angle = -1

    def consume_powerup(self, powerup=None, index=None):
        """
        consumes the passed powerup, applying its effect and removing it from the player's inventory
        :param powerup: the specific powerup to use, must not be passed in if index is
        :param index: the index in the list to consume the powerup, must not be passed in if powerup is
        :return: None
        """
        if powerup is not None and index is not None:
            raise ValueError("Either powerup or index must be none!")
        elif index is not None:
            powerup = self.powerups[index]
        elif powerup is not None:
            index = self.powerups.index(powerup)

        if powerup is not None:
            # get the next index for an empty active powerup slot
            active_index = 0 if self.active_powerups[0] is None else 1 if self.active_powerups[1] is None else -1
            if index > -1:
                powerup.apply_effect()
                self.powerups[index] = None
                self.active_powerups[active_index] = powerup
