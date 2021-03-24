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
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        map_name = "penguin/game/assets/maps/room_1.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room
    
    def setup_room_2(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        map_name = "penguin/game/assets/maps/room_2.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_3(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        map_name = "penguin/game/assets/maps/room_3.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"

        my_map = arcade.tilemap.read_tmx(map_name)


        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)


        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_4(self): # placeholder room
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'big'
        map_name = "penguin/game/assets/maps/room_1.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_5(self): 
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        map_name = "penguin/game/assets/maps/room_5.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_6(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        map_name = "penguin/game/assets/maps/room_6.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_7(self): # placeholder room
        room = Room()
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        map_name = "penguin/game/assets/maps/room_1.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_8(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        map_name = "penguin/game/assets/maps/room_8.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_9(self): # placeholder room
        room = Room()
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        map_name = "penguin/game/assets/maps/room_1.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room