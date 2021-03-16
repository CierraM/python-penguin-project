from game.action import Action
import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this
    class of objects is to draw all actors in the cast.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        

    def execute(self, cast):
        """Executes the action using the given actors. The action in this
        case is to draw each actor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        

        for spritelist in cast:
            spritelist.draw()

        #This specifically draws the health bar for the player
        self.player_sprite = cast[0]
        for player in self.player_sprite:
            player.draw_health_number()
            player.draw_health_bar()

