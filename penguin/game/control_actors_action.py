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

    def __init__(self, input_service, director):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self.director = director
        self._input_service = input_service
        self.min_distance = 100
        self.boss_move_x = 7
        self.boss_move_y = -50
        self.boss_wall_hits = 0
        # self.fire_speed = 10
        self.bullet_buffer = 9
        self.max_distance_apart_x = 100
        self.max_distance_apart_y = 100
        self.follower_offset = 21
        self.follower_turn = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        move_boss = len(player_sprite_list) > 1
        if move_boss:
            boss_sprite = player_sprite_list[1]
        penguin_follower = cast[2]
        bullet_list = cast[3]
        room = self.director.rooms[self.director.current_room]
        room_x = room.width
        room_y = room.height
        follower_bullet_list = cast[5]
        # wall_item = arcade.tilemap.SpriteList[0].center_x
        # wall_list = room.wall_list.
        # penguin_follower_max_x = room.width - 
        # penguin_follower_min_x = room.width

        new_bullet = self._input_service.get_create_bullet()
        new_change_x = self._input_service.get_change_x()
        new_change_y = self._input_service.get_change_y()
        
        if move_boss:
            enemy_bullet_list = cast[4]
            if boss_sprite.center_x >= constants.SCREEN_WIDTH:
                self.boss_move_x = 0 - self.boss_move_x 
                self.boss_wall_hits += 1
            elif boss_sprite.center_x <= 0:
                boss_sprite.center_y += self.boss_move_y
                self.boss_move_x = 0 - self.boss_move_x
                self.boss_move_y = 0 -self.boss_move_y
            boss_sprite.center_x += self.boss_move_x

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

            if penguin_change_x > 0 + 32 and penguin_change_x < room_x - 32: 
                penguin.center_x = penguin_change_x

            if abs(player_sprite.center_x - penguin.center_x) > self.max_distance_apart_x:
                if player_sprite.center_x > penguin.center_x:
                    penguin.center_x = player_sprite.center_x + self.follower_offset
                else: 
                    penguin.center_x = player_sprite.center_x - self.follower_offset 
            # Keep penguins from crowding player's face
            if (penguin.right < player_sprite.right and penguin.right > player_sprite.center_x):
                penguin.right += 16
            if (penguin.right > player_sprite.left and penguin.right < player_sprite.center_x):
                penguin.right -= 16
            
            if penguin_change_y > 0 + 32 and penguin_change_y < room_y - 32: 
                penguin.center_y = penguin_change_y

            if abs(player_sprite.center_y - penguin.center_y) > self.max_distance_apart_y:
                if player_sprite.center_y > penguin.center_y:
                    penguin.center_y = player_sprite.center_y + self.follower_offset
                else: 
                    penguin.center_y = player_sprite.center_y - self.follower_offset 

            # delta_x = player_sprite.center_x - penguin.center_x
            # penguin.center_x = self.move_follower(delta_x,player_sprite.center_x)
            # delta_y = player_sprite.center_y - penguin.center_y
            # penguin.center_y = self.move_follower(delta_y,player_sprite.center_y)

        #This creates a new bullet and gives it attributes
        # if new_bullet and self.fire_speed == 0:
        if new_bullet:
            self.bullet_buffer += 1
            if self.bullet_buffer % 10 == 0:
                bullet = arcade.Sprite("penguin/game/assets/graphics/penguinSnowball.png", .18)
                bullet.angle = 0
                bullet.change_y = constants.BULLET_SPEED
                bullet.center_x = player_sprite.center_x
                bullet.bottom = player_sprite.top
                bullet_list.append(bullet)

                if len(penguin_follower) > 0:
                    follower_shot = arcade.Sprite("penguin/game/assets/graphics/penguinSnowball.png", .10)
                    follower_shot.angle = random.randint(-15, 15)
                    follower_shot.change_y = constants.BULLET_SPEED
                    follower_shot.center_x = penguin_follower[self.follower_turn].center_x
                    follower_shot.bottom = penguin_follower[self.follower_turn].top
                    follower_bullet_list.append(follower_shot)
                    self.follower_turn += 1 
                    if self.follower_turn == len(penguin_follower):
                        self.follower_turn = 0
            else:
                pass
        else:
            self.bullet_buffer = 9

        #     bullet.center_x = player_sprite.center_x
        #     bullet.bottom = player_sprite.top

        #     bullet_list.append(bullet)
        #     self.fire_speed = 10
        # else:
        #     self.fire_speed = self.fire_speed - 1
        #     if self.fire_speed < 0:
        #         self.fire_speed = 10

        if move_boss and random.randint(0, 100) > 90:

            bullet = arcade.Sprite("penguin/game/assets/graphics/bossSnowball.png", .15)
            bullet.angle = -90
            bullet.change_y = 0 - constants.BULLET_SPEED
            bullet.top = boss_sprite.center_y
            bullet.center_x = boss_sprite.center_x
            enemy_bullet_list.append(bullet)
        if move_boss and len(enemy_bullet_list) > 0:
            enemy_bullet_list.update()

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
        
        
