from game import constants
from game.point import Point
import arcade
from game import constants

class Actor:
    """Responsibilities:

    Stereotype:
        Information Holder

    Attributes:
        
    """

    def __init__(self, image, scaling=1):
        """The class constructor.
            image: a url to the image that will represent the sprite
        """
        self._sprite = arcade.Sprite(image, scaling)
        self._sprite.center_x = (constants.SCREEN_WIDTH / 2)
        self._sprite.center_y = (constants.SCREEN_HEIGHT / 2)

    def set_position(x, y):
        self._sprite.center_x =(x)
        self._sprite.center_y =(y)



        