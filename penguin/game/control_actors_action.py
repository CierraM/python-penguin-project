from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # for spritelist in cast:
        #     self._input_service.get_change_x(spritelist)
        #This needs to be updated a bit so that it can be used for all of the sprites and not just
        #The player_sprite
        # for spritelist in cast:
                #     spritelist.center_x = (spritelist.center_x + self._input_service.get_change_x())
                #     spritelist.center_y = (spritelist.center_y + self._input_service.get_change_y())



        # For now, this works for only moving the main character
        player_sprite = cast[0]
        player_sprite.center_x = (player_sprite.center_x + self._input_service.get_change_x())
        player_sprite.center_y = (player_sprite.center_y + self._input_service.get_change_y())

        
        
        


        # self._input_service.get_change_x()
        # self._input_service.get_change_y()
        
        # self.player_sprite.center_x = (self.player_sprite.center_x + self._input_service.player_sprite.change_x)
        # self.player_sprite.center_y = (self.player_sprite.center_y + self._input_service.player_sprite.change_y)
    

        
