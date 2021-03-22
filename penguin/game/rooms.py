from game.room import Room
import arcade
from game import constants
class Rooms:
    """A class for keeping track of our many rooms in the game. Remembers which room the player is in.
    """
    def __init__(self):
        self.current_room = 0
    
    def setup_room_1(self):
        room = Room()

        """Setup and initalize the variables"""
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        map_name = "penguin/game/assets/map/room_1.tmx"

        walls_layer_name = "Object Layer 1"
        background_layer_name = "Tile Layer 1"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=walls_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)
        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_2(self):
        room = Room()
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        


        return room


            