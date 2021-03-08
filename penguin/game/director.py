from time import sleep
from game import constants
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
import arcade

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
        arcade.set_background_color(arcade.color.SPACE_CADET)
        self.set_update_rate(1/30)
         # create the cast {key: tag, value: list}
        cast = {}

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 20)
        position = Point(x, y)
        velocity = Point(10, 0)
        paddle = Actor()
        paddle.set_text("===========")
        paddle.set_position(position)
        paddle.set_velocity(velocity)
        cast["paddle"] = [paddle]

        cast["brick"] = []
        for x in range( int(constants.MAX_X * 0.1), int(constants.MAX_X * 0.9), 10):
            for y in range( int(constants.MAX_Y * 0.6), int(constants.MAX_Y * 0.8), 10):
                position = Point(x, y)
                brick = Actor()
                brick.set_text("*")
                brick.set_position(position)
                cast["brick"].append(brick)

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(10, -10)
        ball = Actor()
        ball.set_text("@")
        ball.set_position(position)
        ball.set_velocity(velocity)
        cast["ball"] = [ball]

        # create the script {key: tag, value: list}
        script = {}

        self.input_service = InputService()
        output_service = OutputService()
        control_actors_action = ControlActorsAction(self.input_service)
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        draw_actors_action = DrawActorsAction(output_service)

        script["input"] =  [control_actors_action]
        script["update"] = [move_actors_action, handle_collisions_action]
        script["output"] = [draw_actors_action]

        self._cast = cast
        self._script = script


    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        arcade.run()


    def on_update(self, delta_time: float):
        self._cue_action("input")
        self._cue_action("update")


    def on_draw(self):
        arcade.start_render()
        self._cue_action("output")


    def on_key_press(self, symbol, modifiers):
        self.input_service.set_symbols(symbol, modifiers)


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)