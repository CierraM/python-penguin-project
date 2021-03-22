# from pyglet.libs.x11.xlib import CapNotLast
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


class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        
        
        # Setup the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BUBBLES)
        self.set_update_rate(1/30)
        self.setup()
        

        
    def setup(self):

        
        self.physics_engine = None
        self.sounds = Sounds()
        self.sounds.play_sound("main_1")

        self.player_list = arcade.SpriteList() # you
        self.follower_list = arcade.SpriteList() # penguins that could follow you
        self.following_list = arcade.SpriteList() # penguins that are following you
        self.player_bullet_list = arcade.SpriteList() # bullets the player shoots
        self.enemy_bullet_list = arcade.SpriteList() # bullets the boss shoots

        # Also commented this out until we finish the following_list
        #self.following_list = arcade.SpriteList() # penguins that are actually following you
    
        #this is the player sprite
        self.player_sprite = SpriteWithHealth("penguin/game/assets/graphics/penguin.png", .25, max_health = 3) # this function give the sprite a health bar
        self.player_sprite.center_x = (constants.SCREEN_WIDTH / 2)
        self.player_sprite.center_y = (constants.SCREEN_HEIGHT / 2)
        self.player_list.append(self.player_sprite)

        #this is the Boss sprite
        self.boss_sprite = SpriteWithHealth("penguin/game/assets/graphics/boss.png", .25, max_health = 10) # this function give the sprite a health bar
        self.boss_sprite.center_x = (constants.SCREEN_WIDTH / 2)
        self.boss_sprite.center_y = (constants.SCREEN_HEIGHT - 150)
        #self.player_list.append(self.boss_sprite)

    
        for x in range(random.randint(1, 10)):      
            self.follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            self.follower.center_x = (random.randint(1, constants.SCREEN_WIDTH)) 
            self.follower.center_y = (random.randint(1, constants.SCREEN_HEIGHT))
            self.follower_list.append(self.follower)



        self._cast = []
        self._cast.append(self.player_list)
        #use player list not player so you can use the list function in the arcade library
        self._cast.append(self.follower_list)
        self._cast.append(self.following_list)
        self._cast.append(self.player_bullet_list)
        self._cast.append(self.enemy_bullet_list)

        # Add room setup to the cast also
        self.setup_rooms()
        # create the script {key: tag, value: list}
        self._script = {}

        self.input_service = InputService()

        # output_service.draw_actors(cast["avatar"])
        control_actors_action = ControlActorsAction(self.input_service)
        
        handle_collisions_action = HandleCollisionsAction(self)
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


    def on_draw(self):
        arcade.start_render()
        if self.rooms[self.current_room].background:
            self.rooms[self.current_room].background.draw()
        self._cue_action("output")
        # If you want to draw text on the screen put it here
        

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
    
        self.current_room = self.all_rooms.current_room
        self._cast.append(self.rooms[self.current_room].wall_list)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
        

    def update_room(self, prev, new):
        self.physics_engine.update()
        self._cast.remove(self.rooms[prev].wall_list)
        self.all_rooms.current_room = new
        self.current_room = self.all_rooms.current_room
        self._cast.append(self.rooms[self.current_room].wall_list)
        if new == 1:
            self.player_list.append(self.boss_sprite)
        else:
            self.player_list.remove(self.boss_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
        
        