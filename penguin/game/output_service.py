import sys
from game import constants
import arcade

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the screen. 
    
    Stereotype: 
        Service Provider

    Attributes:
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        

    def draw_actors(self, actors):
        """Renders the given spritelist to the screen.

        Args:
            actors (spritelist): The actors to render.
        """ 
        actors.draw()