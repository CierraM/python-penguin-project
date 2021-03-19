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

        #Loop to create walls
        for y in (0, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE):
            for x in range(0, constants.SCREEN_WIDTH, constants.SPRITE_SIZE):
                wall = arcade.Sprite("penguin/game/assets/graphics/ice-block.png", constants.SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
        for x in (0, constants.SCREEN_WIDTH - constants.SPRITE_SIZE):
        # Loop for each box going across

            for y in range(constants.SPRITE_SIZE, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE, constants.SPRITE_SIZE):
                # Skip making a block 4 and 5 blocks up on the right side
                if (y != constants.SPRITE_SIZE * 4 and y != constants.SPRITE_SIZE * 5) or x == 0:
                    wall = arcade.Sprite("penguin/game/assets/graphics/ice-block.png", constants.SPRITE_SCALING)
                    wall.left = x
                    wall.bottom = y
                    room.wall_list.append(wall)

            wall = arcade.Sprite("penguin/game/assets/graphics/ice-block.png", constants.SPRITE_SCALING)
            wall.left = 7 * constants.SPRITE_SIZE
            wall.bottom = 5 * constants.SPRITE_SIZE
            room.wall_list.append(wall)

            return room

    def setup_room_2(self):
        room = Room()
        map_name = "penguin/game/assets/maps/map2.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room


            