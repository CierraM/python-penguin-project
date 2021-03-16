import sys
import arcade

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._symbol = ""
        self._modifiers = ""
        self.sprite_change_x = 0
        self.sprite_change_y = 0
        
    def key_press(self, symbol, modifiers):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """

        self._symbol = symbol
        self._modifiers = modifiers

        if self._symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if self._symbol == arcade.key.A or self._symbol == arcade.key.LEFT:
            self.sprite_change_x = -10

        if self._symbol == arcade.key.D or self._symbol == arcade.key.RIGHT:
            self.sprite_change_x = 10

        if self._symbol == arcade.key.W or self._symbol == arcade.key.UP:
            self.sprite_change_y = 10

        if self._symbol == arcade.key.S or self._symbol == arcade.key.DOWN:
            self.sprite_change_y = -10

    def key_release(self, symbol, modifiers):

        self._symbol = symbol
        self._modifiers = modifiers

        if (
            self._symbol == arcade.key.A 
            or self._symbol == arcade.key.LEFT 
            or self._symbol == arcade.key.D 
            or self._symbol == arcade.key.RIGHT
        ):
            self.sprite_change_x = 0

        if (
            self._symbol == arcade.key.W 
            or self._symbol == arcade.key.UP 
            or self._symbol == arcade.key.S 
            or self._symbol == arcade.key.DOWN
        ):
            self.sprite_change_y = 0

    def get_change_x(self):
        return self.sprite_change_x

    def get_change_y(self):
        return self.sprite_change_y

    # def set_symbols(self, symbol, modifiers):
    #     self._symbol = symbol
    #     self._modifiers = modifiers
