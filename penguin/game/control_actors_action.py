from game import constants
from game.action import Action
import arcade
import random

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self.min_distance = 100
        self.bullet_buffer = 9

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        # For now, this works for only moving the main character
        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        penguin_follower = cast[2]
        bullet_list = cast[3]
        new_bullet = self._input_service.get_create_bullet()
        new_change_x = self._input_service.get_change_x()
        new_change_y = self._input_service.get_change_y()
        

        changex = player_sprite.center_x + new_change_x
        player_sprite.center_x = changex
        changey = player_sprite.center_y + new_change_y
        player_sprite.center_y = changey

        for penguin in penguin_follower:
            penguin_change_x = new_change_x + random.randint(-5, 5) + penguin.center_x
            penguin_change_y = new_change_y + random.randint(-4, 4) + penguin.center_y
            #the following two lines of code will slow penguin movement
            # move = random.randint(0, 1)
            # if move == 0:

            if penguin_change_x > 0 and penguin_change_x < constants.SCREEN_WIDTH: 
                penguin.center_x = penguin_change_x

            if penguin_change_y > 0 and penguin_change_y < constants.SCREEN_HEIGHT: 
                penguin.center_y = penguin_change_y

            # delta_x = player_sprite.center_x - penguin.center_x
            # penguin.center_x = self.move_follower(delta_x,player_sprite.center_x)
            # delta_y = player_sprite.center_y - penguin.center_y
            # penguin.center_y = self.move_follower(delta_y,player_sprite.center_y)

        #This creates a new bullet and gives it attributes
        if new_bullet:
            self.bullet_buffer += 1
            if self.bullet_buffer % 10 == 0:
                bullet = arcade.Sprite("penguin/game/assets/graphics/penguinSnowball.png", .18)

                bullet.angle = 90

                bullet.change_y = constants.BULLET_SPEED

                bullet.center_x = player_sprite.center_x
                bullet.bottom = player_sprite.top

                bullet_list.append(bullet)
            else:
                pass
        else:
            self.bullet_buffer = 9

    def move_follower(self,delta,center):
        move = random.randint(0, 50)
        if move == 0:
            return center
        if delta < self.min_distance:
            if delta < 0:
                center += random.randint(delta, 0)
            else:
                center += random.randint(0, delta)
        else: 
            if delta < 0:
                center -= random.randint(delta, 0)
            else:
                center -= random.randint(0, delta)
        return center
        
        
