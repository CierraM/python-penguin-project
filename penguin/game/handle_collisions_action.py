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
        move_boss = len(player_sprite_list) > 1
        if move_boss:
            boss_sprite = player_sprite_list[1]
        enemy_bullet_list = cast[4]
        
        
        #Collision handling for big penguin with little penguin
        player_bullet_list = cast[3]
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
         #Go from room 1 to room 2
        if player_sprite.center_x > self.director.rooms[self.director.current_room].width and self.director.current_room == 0:
            self.director.update_room(1, 2)
            move_boss = False
            player_sprite.center_x = 0
            player_sprite.center_y = self.director.rooms[self.director.current_room].height / 2
            for follower in follower_list:
                follower.center_x = 0
                follower.center_y = self.director.rooms[self.director.current_room].height / 2
        
        #Go from room 2 to room 1
        elif player_sprite.center_x < 0 and self.director.current_room == 1:
            self.director.update_room(2, 1)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width
        
        #Go from room 1 to room 3
        
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height and self.director.current_room == 0:
            self.director.update_room(1, 3)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = 0
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = 0
            
        #Go from room 3 to room 1
        elif player_sprite.center_y < 0 and self.director.current_room == 2:
            self.director.update_room(3, 1)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = self.director.rooms[self.director.current_room].height
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = self.director.rooms[self.director.current_room].height

        # self.following = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
        # self.following.center_x = 20 + (constants.SCREEN_WIDTH / 2) 
        # self.following.center_y = 20 + (constants.SCREEN_HEIGHT / 2)
        # self.following_list.append(self.following)


        #This code is created for the player's bullets to hit the boss
        player_bullet_list.update()
        for bullet in player_bullet_list:
            if move_boss:
                hit_list_1 = arcade.check_for_collision_with_list(bullet, player_sprite_list)
                if len(hit_list_1) > 0:
                    bullet.remove_from_sprite_lists()
                for hit in hit_list_1:
                    #remove 1 point of health per hit
                    boss_sprite.cur_health -= 1

                    if boss_sprite.cur_health <= 0:
                        #Dead
                        self.sounds.play_sound("boss-death")
                        boss_sprite.remove_from_sprite_lists()
                    else:
                        #Not dead
                        self.sounds.play_sound("boss-hit")
            if bullet.bottom > constants.SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        #This code is for the boss's bullets to hit the player
        enemy_bullet_list.update()
        if move_boss:
            hit_list_2 = arcade.check_for_collision_with_list(player_sprite, enemy_bullet_list)
            for bullet in hit_list_2:
                bullet.remove_from_sprite_lists()

                #remove 1 point of health per hit
                player_sprite.cur_health -= 1

                if player_sprite.cur_health <= 0:
                    #Dead
                    self.sounds.play_sound("player-death")
                else:
                    #Not dead
                    self.sounds.play_sound("player-hit")

                # if player_sprite.cur_health <= 0:
                #     #insert code for death/end game
                #     pass
                # else:
                #     #insert sound for taking a hit
                #     pass
                
                if bullet.bottom < 0:
                    bullet.remove_from_sprite_lists()
        
