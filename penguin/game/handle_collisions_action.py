import random
import arcade
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def __init__(self, director):
        self.director = director

    def execute(self, cast):
        self.director.physics_engine.update()
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        small_penguin_list = cast[1]
        small_penguin_list.update()
        follower_list = cast[2]
        
        
        #Collision handling for big penguin with little penguin
        # # Generate a list of all sprites that collided with the player.
        penguin_hit_list = arcade.check_for_collision_with_list(player_sprite, small_penguin_list)
        # Loop through each colliding sprite, and append to follower list
        for penguin in penguin_hit_list:
            penguin.remove_from_sprite_lists()
            follower_list.append(penguin) 
            penguin.center_x = player_sprite.center_x + random.randint(-20, 40)
            penguin.center_y = player_sprite.center_y + random.randint(-20, 40)

         # Collision handling for switching rooms:
        if player_sprite.center_x > constants.SCREEN_WIDTH and self.director.current_room == 0:
            self.director.update_room(0, 1)
            player_sprite.center_x -= constants.SCREEN_WIDTH
            for follower in follower_list:
                follower.center_x -= constants.SCREEN_WIDTH
        
        elif player_sprite.center_x < 0 and self.director.current_room == 1:
            self.director.update_room(1, 0)
            player_sprite.center_x += constants.SCREEN_WIDTH
            for follower in follower_list:
                follower.center_x += constants.SCREEN_WIDTH
            