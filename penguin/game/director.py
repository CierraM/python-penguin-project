from game import constants
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
import arcade
from game import constants
from game.sounds import Sounds
import random

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
        self.sounds = Sounds()
        self.sounds.play_sound("main_1")

        self.player_list = arcade.SpriteList() # you
        self.follower_list = arcade.SpriteList() # penguins that could follow you
        self.following_list = arcade.SpriteList() #penguins that are following you

        # Also commented this out until we finish the following_list
        # self.following_list = arcade.SpriteList() # penguins that are actually following you
        
        self.player_sprite = arcade.Sprite("penguin/game/assets/graphics/penguin.png", .25)
        self.player_sprite.center_x = (constants.SCREEN_WIDTH / 2)
        self.player_sprite.center_y = (constants.SCREEN_HEIGHT / 2)
        self.player_list.append(self.player_sprite)

    
        for x in range(random.randint(1, 10)):      
            self.follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            self.follower.center_x = (random.randint(1, constants.SCREEN_WIDTH)) 
            self.follower.center_y = (random.randint(1, constants.SCREEN_HEIGHT))
            self.follower_list.append(self.follower)



        self._cast = []
        self._cast.append(self.player_list)
        #use player list not player so you can use the list function in the arcade library

        # I commented the follower and the following lists until we give them more details
        # As is, these two break the code without anything in them.
        self._cast.append(self.follower_list)
        self._cast.append(self.following_list)

        # create the script {key: tag, value: list}
        self._script = {}

        self.input_service = InputService()
        output_service = OutputService()
        # output_service.draw_actors(cast["avatar"])
        control_actors_action = ControlActorsAction(self.input_service)
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        draw_actors_action = DrawActorsAction(output_service)

        self._script["input"] =  [control_actors_action]
        self._script["update"] = [move_actors_action, handle_collisions_action]
        self._script["output"] = [draw_actors_action]

        

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        arcade.run()


    def on_update(self, delta_time: float):
        self._cue_action("input")
        self._cue_action("update")


    def on_draw(self):
        arcade.start_render()
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