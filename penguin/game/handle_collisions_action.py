import random
import arcade
from game import constants
from game.action import Action
from game.sounds import Sounds


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def __init__(self, director):
        self.director = director
        self.sounds = Sounds()

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
        player_bullet_list = cast[3]
        enemy_bullet_list = cast[4]
        # penguin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.follower_list)  
        # # Generate a list of all sprites that collided with the player.
        penguin_hit_list = arcade.check_for_collision_with_list(player_sprite, small_penguin_list)
        # Loop through each colliding sprite, and append to follower list
        for penguin in penguin_hit_list:
            penguin.remove_from_sprite_lists()
            follower_list.append(penguin) 
            penguin.center_x = player_sprite.center_x + random.randint(-20, 40)
            penguin.center_y = player_sprite.center_y + random.randint(-20, 40)
            self.sounds.play_sound("penguin-hit")

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
            
        # self.following = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
        # self.following.center_x = 20 + (constants.SCREEN_WIDTH / 2) 
        # self.following.center_y = 20 + (constants.SCREEN_HEIGHT / 2)
        # self.following_list.append(self.following)


        #This code is created for the player's bullets to hit the boss
        player_bullet_list.update()
        for bullet in player_bullet_list:
            #hit_list_1 = arcade.check_for_collision_with_list(bullet, #Whatever we want)
            # if len(hit_list) > 0:
            #     bullet.remove_from_sprite_lists()
            
            if bullet.bottom > constants.SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        #This code is for the boss's bullets to hit the player
        enemy_bullet_list.update()
        for bullet in enemy_bullet_list:
            hit_list_2 = arcade.check_for_collision_with_list(bullet, player_sprite)
            if len(hit_list_2) > 0:
                bullet.remove_from_sprite_lists()
            
            if player_sprite.cur_health <= 0:
                #insert code for death/end game
                pass
            else:
                #insert sound for taking a hit
                pass
            
            if bullet.bottom < constants.SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
        
