import random
import arcade
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        small_penguin_list = cast[1]
        follower_list = cast[2]
        # # Generate a list of all sprites that collided with the player.
        penguin_hit_list = arcade.check_for_collision_with_list(player_sprite, small_penguin_list)
        # Loop through each colliding sprite, and append to follower list
        for penguin in penguin_hit_list:
            penguin.remove_from_sprite_lists()
            follower_list.append(penguin)
        # self.following = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
        # self.following.center_x = 20 + (constants.SCREEN_WIDTH / 2) 
        # self.following.center_y = 20 + (constants.SCREEN_HEIGHT / 2)
        # self.following_list.append(self.following)