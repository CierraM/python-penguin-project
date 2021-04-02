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
        self.max_distance_apart_x = 200
        self.max_distance_apart_y = 200
        self.follower_offset = 21
        self.follower_turn = 0
        self.hard_mode_on = True

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #Cast: [player, player bullet, enemy bullet, follower bullet, following list, follower list, walls]
        player_sprite_list = cast[0]
        player_sprite = player_sprite_list[0]
        move_boss = len(player_sprite_list) > 1
        if move_boss:
            boss_sprite = player_sprite_list[1]
        penguin_follower = cast[4]
        bullet_list = cast[1]
        room = self.director.rooms[self.director.current_room]
        room_x = room.width
        room_y = room.height
        follower_bullet_list = cast[3]


        new_bullet = self._input_service.get_create_bullet()
        new_change_x = self._input_service.get_change_x()
        new_change_y = self._input_service.get_change_y()
        player_sprite.update(new_change_x, new_change_y)
        
        if move_boss:
            if boss_sprite.cur_health <= 75:
                if self.hard_mode_on:
                    self.boss_move_x = constants.FINAL_MOVEMENT_SPEED
                    self.hard_mode_on = False
            enemy_bullet_list = cast[2]
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

        penguin_army_col = 3
        army_right = 1
        current_col = 1
        current_row = 1
        space_col = 20
        for penguin in penguin_follower:
            if move_boss:
                penguin_change_x = new_change_x + army_right * current_col * space_col + player_sprite.center_x
                penguin_change_y = new_change_y + player_sprite.center_y + current_row * space_col + space_col
                current_col += 1 
                if current_col > penguin_army_col:
                    army_right = 0 - army_right
                    current_col = 1
                    if army_right == 1:
                        current_row += 1


            else:

                penguin_change_x = new_change_x + random.randint(-5, 5) + penguin.center_x
                penguin_change_y = new_change_y + random.randint(-4, 4) + penguin.center_y
            #the following two lines of code will slow penguin movement


            if penguin_change_x > 0 + 32 and penguin_change_x < room_x - 32: 
                penguin.center_x = penguin_change_x

            if abs(player_sprite.center_x - penguin.center_x) > self.max_distance_apart_x:
                if player_sprite.center_x > penguin.center_x:
                    penguin.center_x = player_sprite.center_x + self.follower_offset
                else: 
                    penguin.center_x = player_sprite.center_x - self.follower_offset 
            # Keep penguins from crowding player's face
            if (penguin.right < player_sprite.right and penguin.right > player_sprite.center_x):
                penguin.right -= 32
            if (penguin.right > player_sprite.left and penguin.right < player_sprite.center_x):
                penguin.right += 32
            
            if penguin_change_y > 0 + 32 and penguin_change_y < room_y - 32: 
                penguin.center_y = penguin_change_y

            if abs(player_sprite.center_y - penguin.center_y) > self.max_distance_apart_y:
                if player_sprite.center_y > penguin.center_y:
                    penguin.center_y = player_sprite.center_y + self.follower_offset
                else: 
                    penguin.center_y = player_sprite.center_y - self.follower_offset 

        #This creates a new bullet and gives it attributes
        artifact_num = self.director.collected_artifacts
        if new_bullet:
            self.bullet_buffer += 1
            if self.bullet_buffer % 10 == 0:
                bullet = arcade.Sprite("penguin/game/assets/graphics/penguinSnowball.png", .18)
                bullet.angle = 0
                bullet.change_y = constants.BULLET_SPEED * (artifact_num + 1)
                bullet.center_x = player_sprite.center_x
                bullet.bottom = player_sprite.top
                bullet_list.append(bullet)

                if len(penguin_follower) > 0:
                    follower_shot = arcade.Sprite("penguin/game/assets/graphics/penguinSnowball.png", .10)
                    follower_shot.angle = random.randint(-15, 15)
                    follower_shot.change_y = constants.BULLET_SPEED
                    try:
                        follower_shot.center_x = penguin_follower[self.follower_turn].center_x
                        follower_shot.bottom = penguin_follower[self.follower_turn].top
                    except:
                       x = 1
                    follower_bullet_list.append(follower_shot)
                    self.follower_turn += 1 
                    if self.follower_turn >= len(penguin_follower):
                        self.follower_turn = 0
            else:
                pass
        else:
            self.bullet_buffer = 9

        if move_boss and random.randint(0, 100) > 90:

            bullet = arcade.Sprite("penguin/game/assets/graphics/bossSnowball.png", .15)
            bullet.angle = -90
            if boss_sprite.cur_health <= 75:
                bullet.change_y = 0 - constants.FINAL_BULLET_SPEED
            else:
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
        
        
