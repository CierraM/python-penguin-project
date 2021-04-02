# from pyglet.libs.x11.xlib import CapNotLast
from pyglet.window.key import S
from game import constants
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.input_service import InputService
from game.handle_health import SpriteWithHealth
import arcade
from game import constants
from game.sounds import Sounds
import random
from game.rooms import Rooms
import time
from game.player import Player
import sys

class IntroView(arcade.View):
    """View to intro the game"""

    def __init__(self):
        """This will run once the view is set"""
        super().__init__()
        self.texture = arcade.load_texture("penguin/game/assets/graphics/game_start.png")

        # arcade.set_background_color(arcade.color.BUBBLES)

        #Reset the viewport, necessary if we have a scrolling game and we need
        #to reset the viewport back to the start so we can see what we draw
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def setup(self):
        """Add Music"""
        self.sounds = Sounds()
        self.soundtracks = Sounds() #For music
        self.soundtracks.play_sound("intro_screen")

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_key_press(self, symbol, modifiers):
        self._symbol = symbol
        self._modifiers = modifiers

        if self._symbol == arcade.key.SPACE:
            if self.soundtracks.get_current_sound() != None:
                self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
            self.sounds.play_sound("game_start")
            game_view = DirectorView()
            game_view.setup()
            self.window.show_view(game_view)

class VictoryView(arcade.View):
    """View victory screen for beating the game"""

    def __init__(self):
        """This will run once the view is set"""
        super().__init__()
        self.texture = arcade.load_texture("penguin/game/assets/graphics/completeEnd.png")

        # arcade.set_background_color(arcade.color.BUBBLES)

        #Reset the viewport, necessary if we have a scrolling game and we need
        #to reset the viewport back to the start so we can see what we draw
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def setup(self):
        """Add Music"""
        self.sounds = Sounds()
        self.soundtracks = Sounds() #For music
        self.soundtracks.play_sound("end_screen")

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, (constants.SCREEN_HEIGHT / 2) - 10, 1200, 690)

    def on_key_press(self, symbol, modifiers):
        self._symbol = symbol
        self._modifiers = modifiers

        if self._symbol == arcade.key.ESCAPE:
            self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
            self.sounds.play_sound("gg")
            time.sleep(.65)
            arcade.close_window()

class GameOverView(arcade.View):
    """View to show when game is over"""

    def __init__(self):
        """This will run once the view is set"""
        super().__init__()
        self.texture = arcade.load_texture("penguin/game/assets/graphics/end.png")

        # arcade.set_background_color(arcade.color.BLACK)

        #Reset the viewport, necessary if we have a scrolling game and we need
        #to reset the viewport back to the start so we can see what we draw
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def setup(self):
        """Add Music"""
        self.sounds = Sounds()
        # self.soundtracks = Sounds() #For music
        # self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
        time.sleep(0.1)
        self.sounds.play_sound("gameover")

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_key_press(self, symbol, modifiers):
        self._symbol = symbol
        self._modifiers = modifiers

        if self._symbol == arcade.key.SPACE:
            self.sounds.stop_sound(self.sounds.get_current_sound())
            self.sounds.play_sound("game_start")
            game_view = DirectorView()
            game_view.setup()
            self.window.show_view(game_view)


class DirectorView(arcade.View):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        
        
        # Setup the window
        super().__init__()
        arcade.set_background_color(arcade.color.BUBBLES)
        # self.set_update_rate(1/30)
        self.view_bottom = 0
        self.view_left = 0
        # self.setup()
        

        
    def setup(self):

        
        self.physics_engine = None
        self.sounds = Sounds() #For sound effects
        self.soundtracks = Sounds() #For music
        #To let the game start sound finish, pause for 1.5 seconds
        time.sleep(1.7)
        self.soundtracks.play_sound("main_theme")

        self.collected_artifacts = 0
        self.artifact_1_collected = False
        self.artifact_2_collected = False

        # Keep track of scrolling
        self.view_bottom =704
        self.view_left = 1184

        # Use these to tell the game where to start your scroll off?
        self.top = 350
        self.right = 600
        self.bottom = 350
        self.left = 600

        self.punnum = 0

        self.player_list = arcade.SpriteList() # you
        self.follower_list = arcade.SpriteList() # penguins that could follow you
        self.following_list = arcade.SpriteList() # penguins that are following you
        self.player_bullet_list = arcade.SpriteList() # bullets the player shoots
        self.enemy_bullet_list = arcade.SpriteList() # bullets the boss shoots
        self.follower_bullet_list = arcade.SpriteList() #bullets the follower penguins shoot
        self.npc_list = arcade.SpriteList() #NPC village penguins

        
        #this is the player sprite
        
        self.player_sprite = Player("penguin/game/assets/graphics/penguin.png", .25, 32, 33, -10, 11, 40, 5,  max_health = 5) # this function give the sprite a health bar
        self.player_sprite.center_x = (1150)
        self.player_sprite.center_y = (704)
        
        self.player_list.append(self.player_sprite)

        #this is the Boss sprite
        self.boss_sprite = SpriteWithHealth("penguin/game/assets/graphics/boss.png", .24, -90, -110, -22, 14, 80, 7, max_health = 1) # this function give the sprite a health bar
        self.boss_sprite.center_x = (constants.SCREEN_WIDTH / 2)
        self.boss_sprite.center_y = (constants.SCREEN_HEIGHT - 210)
        

        #Create artifacts, but don't append it yet
        self.artifact_list = arcade.SpriteList()

        self._cast = []
        self._cast.append(self.player_list)
        #use player list not player so you can use the list function in the arcade library
        # self._cast.append(self.follower_list)
        
        self._cast.append(self.player_bullet_list)
        self._cast.append(self.enemy_bullet_list)
        self._cast.append(self.follower_bullet_list)
        self._cast.append(self.following_list)
        # Add room setup to the cast also
        self.setup_rooms() # adds followers, then walls
        #Cast: [player, player bullet, enemy bullet, follower bullet, following list, follower list, walls]

        
            
        # create the script {key: tag, value: list}
        self._script = {}
        # passing variables
        self.input_service = InputService()
        self.game_over = GameOverView()
        self.victory_view = VictoryView()

        # output_service.draw_actors(cast["avatar"])
        control_actors_action = ControlActorsAction(self.input_service, self)
        handle_collisions_action = HandleCollisionsAction(self, self.game_over, self.victory_view, self.soundtracks)
        draw_actors_action = DrawActorsAction()

        self._script["input"] =  [control_actors_action]
        self._script["update"] = [handle_collisions_action]
        self._script["output"] = [draw_actors_action]

        
        

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        arcade.run()


    def on_update(self, delta_time: float):
        self._cue_action("input")
        self._cue_action("update")
        if self.rooms[self.current_room] == 8:
            self.npc_talk()
        #Handle scrolling and viewport positioning:
        if self.rooms[self.current_room].size == 'big':

            if self.player_sprite.center_x == 0:
                left = 0
            else:
                left = self.rooms[self.current_room].width - constants.SCREEN_WIDTH

            if self.player_sprite.center_x == self.rooms[self.current_room].width:
                right = self.rooms[self.current_room].width
            else:
                right = constants.SCREEN_WIDTH

            if self.player_sprite.center_y == self.rooms[self.current_room].height:
                top = self.rooms[self.current_room].height
            else:
                top = constants.SCREEN_HEIGHT

            if self.player_sprite.center_y == 0:
                bottom = 0
            else:
                bottom = self.rooms[self.current_room].height - constants.SCREEN_HEIGHT

            arcade.set_viewport(left, right, bottom, top)
            self.scroll()
        else:
            arcade.set_viewport(0, self.rooms[self.current_room].width, 0, self.rooms[self.current_room].height)
        


    def on_draw(self):
        arcade.start_render()       
        self.rooms[self.current_room].background.draw()

        self._cue_action("output")
        # If you want to draw text on the screen put it here
        if self.current_room == 8:
            self.npc_talk()

    def on_key_press(self, symbol, modifiers):
        self.input_service.key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        self.input_service.key_release(symbol, modifiers)


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        
        for action in self._script[tag]:
            action.execute(self._cast)

    def setup_rooms(self):
        self.all_rooms = Rooms()
        self.rooms = []

        room = self.all_rooms.setup_room_1()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_2()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_3()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_4()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_5()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_6()
        self.rooms.append(room)   
        room = self.all_rooms.setup_room_7()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_8()
        self.rooms.append(room)
        room = self.all_rooms.setup_room_9()
        self.rooms.append(room)
    
        self.current_room = self.all_rooms.current_room
        self._cast.append(self.rooms[self.current_room].follower_list)
        self._cast.append(self.rooms[self.current_room].wall_list)
        
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
        
        

    def update_room(self, prev, new):
        
        self.physics_engine.update()
        

        self._cast.remove(self.rooms[prev-1].wall_list)
        self._cast.remove(self.rooms[prev-1].follower_list)
        # self.rooms[prev-1].follower_num -= num

        self.all_rooms.current_room = new-1
        self.current_room = self.all_rooms.current_room
        
        self._cast.append(self.rooms[self.current_room].follower_list)
        self._cast.append(self.rooms[self.current_room].wall_list)


        if not (self.rooms[self.current_room].soundtrack == self.soundtracks.get_current_sound()):
            self.soundtracks.stop_sound(self.soundtracks.get_current_sound())
            self.soundtracks.play_sound(self.rooms[self.current_room].soundtrack)

            
        elif self.boss_sprite in self.player_list:
            self.player_list.remove(self.boss_sprite)
            
        if new == 7:
            self._cast.append(self.rooms[6].background2)

        if prev == 7:
            self._cast.remove(self.rooms[6].background2)

        if new == 8:
            self.player_list.append(self.boss_sprite)

        if new == 9:
            self.punnum = random.randint(0, 3)

        if new == 5 and (not self.artifact_1_collected):
            artifact1 = arcade.Sprite('penguin/game/assets/graphics/potion.png', .2) #Artifact for room 5
            artifact1.center_x = 592
            artifact1.center_y = 100
            self.artifact_list.append(artifact1)
            self._cast.append(self.artifact_list)
        

        if new == 7 and (not self.artifact_2_collected):
            artifact2 = arcade.Sprite('penguin/game/assets/graphics/potion.png', .2) #Artifact for room 7
            artifact2.center_x = 250
            artifact2.center_y = 250
            self.artifact_list.append(artifact2)
            self._cast.append(self.artifact_list)
            

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
        

        
    def scroll(self):
        
        # Scrolling
        changed = False
        # Scroll left
        left_boundary = self.view_left + self.left
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - self.right
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - self.top

        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + self.bottom
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)


    def npc_talk(self):
        # start_x and start_y make the start point for the text. We draw a dot to make it easy too see
        # the text in relation to its start x and y.
        player = self.player_sprite
        
        #Jane
        text1 = """                Jane: \n
                What, you're here to save us from King Silverclaw? \n
                Wow, that's great news! Don't go alone though. He \n
                is dangerous! Please explore penguinland and see \n
                if you can gather up some followers first. They \n
                will help you in the battle. There are a lot of \n
                brave penguins in these parts. Maybe you've met \n
                some of them already."""
        
        if abs(507 - player.center_x) < 100 and abs(381 - player.center_y) < 100:
            #x, y, of bottom left corner, width, and height
            arcade.draw_xywh_rectangle_filled(507, 400, 500, 280, arcade.color.WHITE)
            arcade.draw_text(text1, 507, 430, arcade.color.BLACK, 14)

        #Cierra
        text2 = """                    Cierra: \n
                    Hi, you're new around here, aren't you? \n
                    Let me just warn you, in the area to the \n
                    left of the penguinville there are some warning \n
                    signs North of the pathway. Don't go that way! \n
                    There is an angry polar bear king, and he \n
                    doesn't like visitors. Be careful out there.
                """
        if abs(2075 - player.center_x) < 150 and abs(266 - player.center_y) < 150:
            #x, y, of bottom left corner, width, and height
            arcade.draw_xywh_rectangle_filled(1846, 311, 500, 250, arcade.color.WHITE)
            arcade.draw_text(text2, 1846, 310, arcade.color.BLACK, 14)
        

        #Jacob
        puns = ["I had the best ice pun to tell you… Problem is, it slipped my mind.", "What do you call a cold penguin?A Brrr-d", "Where do penguins go dancing? The Snow Ball.", "What happens when you’re alone and you get too cold? You’re totally ice-olated.", "What do you get when you cross a snowman with a vampire? Frostbite."]
        pun = puns[self.punnum]
        text3 = f'''                  Jacob: \n
                 Hey, you wanna hear a joke? \n
                 {pun} \n
                 Haha!\n
                 Oh by the way, I heard about some cool potion you can\n
                 find that will let you throw snowballs super fast!\n
                 I've honestly never found one myself, but who knows,\n
                 maybe if you look around enough, you'll get lucky!\n
        '''
        if abs(522 - player.center_x) < 150 and abs(1076 - player.center_y) < 150:
            #x, y, of bottom left corner, width, and height
            arcade.draw_xywh_rectangle_filled(550, 1050, 600, 300, arcade.color.WHITE)
            arcade.draw_text(text3, 550, 1050, arcade.color.BLACK, 14)

        #Benjamin
        text4 = """                Benjamin: \n
                It's a dangerous world out there. It's important \n
                for adventurous penguins like you to know how to \n
                defend yourselves. In a pinch, the snow around us \n
                makes a great weapon! Just pack a flipperful of \n
                snow together and press the space bar to throw it. \n
                Don't forget this now! It could save your life! \n
                """
        if abs(1311 - player.center_x) < 100 and abs(764 - player.center_y) < 100:
            #x, y, of bottom left corner, width, and height
            arcade.draw_xywh_rectangle_filled(1330, 790, 500, 250, arcade.color.WHITE)
            arcade.draw_text(text4, 1330, 790, arcade.color.BLACK, 14)