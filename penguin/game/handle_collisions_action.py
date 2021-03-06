import random
import arcade
from game import constants
from game.action import Action
from game.sounds import Sounds
import time


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def __init__(self, director, game_over_view, victory_view, soundtracks):
        self.director = director
        self.sounds = Sounds()
        self.soundtracks = soundtracks
        self.game_over = game_over_view
        self.victory = victory_view

     
    def check_for_collision_with_lists(self, list_1, list_2):
        hit_list = []
        for item in list_1:
            hit_list = arcade.check_for_collision_with_list(item, list_2)
            if len(hit_list) > 0:
                item.remove_from_sprite_lists()
            for bullet in hit_list:
                bullet.remove_from_sprite_lists()
            return   
        

    def execute(self, cast):
        self.director.physics_engine.update()
        
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #Cast: [player, player bullet, enemy bullet, follower bullet, following list, follower list, walls, artifact]
        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        small_penguin_list = cast[5]
        small_penguin_list.update()
        follower_list = cast[4]
        #move boss is true when you're in the boss room
        move_boss = len(player_sprite_list) > 1
        if move_boss:
            boss_sprite = player_sprite_list[1]
        enemy_bullet_list = cast[2]
        follower_bullet_list = cast[3]

        
        #The number of penguins picked up in a room
        
        #Collision handling for big penguin with little penguin
        player_bullet_list = cast[1]
        #
        # # Generate a list of all small penguin sprites that collided with the player.
        penguin_hit_list = arcade.check_for_collision_with_list(player_sprite, small_penguin_list)
        # Loop through each colliding sprite, and append to follower list
        
        for penguin in penguin_hit_list:
            penguin.remove_from_sprite_lists()
            follower_list.append(penguin) 
            penguin.center_x = player_sprite.center_x + random.randint(-20, 40)
            penguin.center_y = player_sprite.center_y + random.randint(-20, 40)
            self.sounds.play_sound("penguin-hit")
        
        #Artifact collision handling:
        # for the cave
        if len(cast) == 9:
            artifact = cast[8][0]
            if arcade.check_for_collision(player_sprite, artifact):
                self.director.collected_artifacts += 1
                self.director.artifact_2_collected = True
                artifact.remove_from_sprite_lists()
                self.sounds.play_sound("artifact")
                cast.pop(8)

        #For the maze
        if len(cast) == 8:
            artifact = cast[7][0]
            if arcade.check_for_collision(player_sprite, artifact):
                self.director.collected_artifacts += 1
                self.director.artifact_1_collected = True
                artifact.remove_from_sprite_lists()
                self.sounds.play_sound("artifact")
                cast.pop(7)
        

        
         # Collision handling for switching rooms:
         #Go from room 1 to room 2
        if player_sprite.center_x > self.director.rooms[self.director.current_room].width and self.director.current_room == 0:
            self.director.update_room(1, 2)
            self.penguin_num = 0
            move_boss = False
            player_sprite.center_x = 0
            player_sprite.center_y = self.director.rooms[self.director.current_room].height / 2
            for follower in follower_list:
                follower.center_x = 0
                follower.center_y = self.director.rooms[self.director.current_room].height / 2
        
        #Go from room 2 to room 1
        elif player_sprite.center_x < 0 and self.director.current_room == 1:
            self.director.update_room(2, 1)
            penguin_num = 0
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width
            player_sprite.center_y = self.director.rooms[self.director.current_room].height /2
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

        #Go from room 3 to room 8
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height and self.director.current_room == 2:
            self.director.update_room(3, 8)
            move_boss = True
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = 0
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = 0

        # Go from room 1 to room 6
        elif player_sprite.center_y < 0 and self.director.current_room == 0:
            self.director.update_room(1, 6)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = self.director.rooms[self.director.current_room].height
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = self.director.rooms[self.director.current_room].height

        #Go from room 6 to room 1
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height and self.director.current_room == 5:
            self.director.update_room(6, 1)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = 0
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = 0

        #Go from room 3 to room 4
        if player_sprite.center_x < 0 and self.director.current_room == 2:
            self.director.update_room(3, 4)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width *1.5
            player_sprite.center_y = 960
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width *1.5
                follower.center_y = 960
    
        #Go from room 4 to room 3
        if player_sprite.center_x > self.director.rooms[self.director.current_room].width *1.5 and self.director.current_room == 3:
            self.director.update_room(4, 3)
            move_boss = False
            player_sprite.center_x = 0
            player_sprite.center_y = self.director.rooms[self.director.current_room].height / 2
            for follower in follower_list:
                follower.center_x = 0
                follower.center_y = self.director.rooms[self.director.current_room].height / 2

        #Go from room 4 to room 5
        elif player_sprite.center_y < 0 and self.director.current_room == 3:
            self.director.update_room(4, 5)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = self.director.rooms[self.director.current_room].height
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = self.director.rooms[self.director.current_room].height

        #Go from room 5 to room 4
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height and self.director.current_room == 4:
            self.director.update_room(5, 4)
            move_boss = False
            player_sprite.center_x = 1450
            player_sprite.center_y = 0
            for follower in follower_list:
                follower.center_x = 1450
                follower.center_y = 0

        #Go from room 5 to room 3
        elif player_sprite.center_x > self.director.rooms[self.director.current_room].width and self.director.current_room == 4:
            self.director.update_room(5, 3)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width /2
            player_sprite.center_y = self.director.rooms[self.director.current_room].height /2
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width /2
                follower.center_y = self.director.rooms[self.director.current_room].height /2
            self.director.sounds.play_sound('teleport')

        #Go from room 6 to room 7 !!!THIS IS THE CAVE ENTRANCE
        elif (player_sprite.center_x <= 620 and player_sprite.center_x >= 603) and (player_sprite.center_y < 400) and self.director.current_room == 5:
            self.director.update_room(6, 7)
            move_boss = False
            player_sprite.center_x = 1268
            player_sprite.center_y = 1220
            for follower in follower_list:
                follower.center_x = 1268
                follower.center_y = 1220

        #Go from room 7 to room 6d
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height -50 and self.director.current_room == 6:
            self.director.update_room(7, 6)
            move_boss = False
            player_sprite.center_x = 615
            player_sprite.center_y = 402
            for follower in follower_list:
                follower.center_x = 615
                follower.center_y = 402

        #Go from room 2 to room 9
        elif player_sprite.center_y > self.director.rooms[self.director.current_room].height and self.director.current_room == 1:
            self.director.update_room(2, 9)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = 0
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = 0

        #Go from room 9 to room 2
        elif player_sprite.center_y < 0 and self.director.current_room == 8:
            self.director.update_room(9, 2)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width / 2
            player_sprite.center_y = self.director.rooms[self.director.current_room].height
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width / 2
                follower.center_y = self.director.rooms[self.director.current_room].height

        #Go from room 3 to room 9
        elif player_sprite.center_x > self.director.rooms[self.director.current_room].width and self.director.current_room == 2:
            self.director.update_room(3, 9)
            move_boss = False
            player_sprite.center_x = 0
            player_sprite.center_y = self.director.rooms[self.director.current_room].height / 2
            for follower in follower_list:
                follower.center_x = 0
                follower.center_y = self.director.rooms[self.director.current_room].height / 2

        #Go from room 9 to room 3
        elif player_sprite.center_x < 0 and self.director.current_room == 8:
            self.director.update_room(9, 3)
            move_boss = False
            player_sprite.center_x = self.director.rooms[self.director.current_room].width
            player_sprite.center_y = self.director.rooms[self.director.current_room].height / 2
            for follower in follower_list:
                follower.center_x = self.director.rooms[self.director.current_room].width
                follower.center_y = self.director.rooms[self.director.current_room].height / 2


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
                        if self.soundtracks.get_current_sound() != None:
                            self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
                        self.sounds.play_sound("boss-death")
                        boss_sprite.remove_from_sprite_lists()
                        time.sleep(1.6)
                        view = self.victory
                        view.setup()
                        self.director.window.show_view(view)
                    else:
                        #Not dead
                        self.sounds.play_sound("boss-hit")  
            if bullet.bottom > constants.SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        #This code is for the boss's bullets to hit the player
        enemy_bullet_list.update()
        if move_boss:

            self.check_for_collision_with_lists(follower_list, enemy_bullet_list)
            hit_list_2 = arcade.check_for_collision_with_list(player_sprite, enemy_bullet_list)
            for bullet in hit_list_2:
                bullet.remove_from_sprite_lists()
                #remove 1 point of health per hit
                player_sprite.cur_health -= 1

                if player_sprite.cur_health <= 0:
                    #Dead
                    self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
                    self.sounds.play_sound("player-death")
                    time.sleep(0.3)
                    view = self.game_over
                    view.setup()
                    self.director.window.show_view(view)

                else:
                    #Not dead
                    self.sounds.play_sound("player-hit")
            
            for bullet in enemy_bullet_list:
                if bullet.bottom < 0:
                    bullet.remove_from_sprite_lists()
        
        move_boss = len(player_sprite_list) > 1
        follower_bullet_list.update()
        if move_boss: 
            boss_sprite = player_sprite_list[1]
            hit_list_1 = arcade.check_for_collision_with_list(boss_sprite, follower_bullet_list)
            for bullet in hit_list_1:
                if len(hit_list_1) > 0:
                    bullet.remove_from_sprite_lists()
                for hit in hit_list_1:
                    #remove 1 point of health per hit
                    boss_sprite.cur_health -= 1

                    if boss_sprite.cur_health <= 0:
                        #Dead
                        if self.soundtracks.get_current_sound() != None:
                            self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
                        self.sounds.play_sound("boss-death")
                        boss_sprite.remove_from_sprite_lists()
                        time.sleep(1.6)
                        move_boss = False 
                        view = self.victory
                        view.setup()
                        self.director.window.show_view(view)
                    else:
                        #Not dead
                        self.sounds.play_sound("boss-hit")
                    if boss_sprite.cur_health == 75:
                        self.sounds.play_sound("boss-death")
                    else:
                        pass
            for bullet in follower_bullet_list:
                if bullet.bottom > constants.SCREEN_HEIGHT:
                    bullet.remove_from_sprite_lists()
    
            