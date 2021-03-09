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
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        arcade.start_render()
        for actor in actors:
            actor.draw()