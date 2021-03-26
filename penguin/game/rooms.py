from game.room import Room
import arcade
import random
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
        room.soundtrack = "main_theme"
        map_name = "penguin/game/assets/maps/room_1.tmx"
        objects_layer_name = "Object Layer 1"
        background_layer_name = "background_color"
        #A function for special setup if needed
        room.specialBehavior = None
        room.follower_num = (random.randint(5, 15))

        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room
    
    def setup_room_2(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        room.soundtrack = "main_theme"
        map_name = "penguin/game/assets/maps/room_2.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(1, 5))

        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_3(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        room.soundtrack = "main_theme"
        map_name = "penguin/game/assets/maps/room_3.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(1, 5))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)


        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)


        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_4(self): 
        room = Room()
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        room.soundtrack = "maze_theme"
        map_name = "penguin/game/assets/maps/room_4.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        room.specialBehavior = None
        room.follower_num = (random.randint(5, 15))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING*1.5, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING*1.5, use_spatial_hash=True)

        return room

    def setup_room_5(self): 
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        room.soundtrack = "main_theme"
        map_name = "penguin/game/assets/maps/room_5.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(1, 5))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_6(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        room.soundtrack = "main_theme"
        map_name = "penguin/game/assets/maps/room_6.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(1, 5))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_7(self): # placeholder room
        room = Room()
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        room.soundtrack = "cave_theme"
        map_name = "penguin/game/assets/maps/room_7.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        background_2 = "background 2"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(5, 15))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)

        my_map = arcade.tilemap.read_tmx(map_name)
        
        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=2, use_spatial_hash=True)
        room.background2 = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_2, scaling=2, use_spatial_hash=True)
        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=2, use_spatial_hash=True)

        

        return room

    def setup_room_8(self):
        room = Room()
        room.width = 1184
        room.height = 672
        room.size = 'small'
        room.soundtrack = "boss_theme"
        map_name = "penguin/game/assets/maps/room_8.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        #A function for special setup if needed
        # room.specialBehavior = self.setupBoss
        room.follower_num = 0
        room.follower_list = arcade.SpriteList()

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        return room

    def setup_room_9(self):
        room = Room()
        room.width = 2368
        room.height = 1344
        room.size = 'big'
        room.soundtrack = "village_theme"
        #A function for special setup if needed
        room.specialBehavior = None

        room.follower_num = (random.randint(5, 25))
        room.follower_list = arcade.SpriteList()

        for x in range(room.follower_num):
            follower = arcade.Sprite("penguin/game/assets/graphics/followerPenguin.png", .15)
            follower.center_x = (random.randint(64, room.width - 64)) 
            follower.center_y = (random.randint(64, room.height - 64))
            room.follower_list.append(follower)
        
        map_name = "penguin/game/assets/maps/room_9.tmx"
        objects_layer_name = "walls"
        background_layer_name = "background"
        

        my_map = arcade.tilemap.read_tmx(map_name)

        room.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name=objects_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        room.background = arcade.tilemap.process_layer(map_object=my_map, layer_name=background_layer_name, scaling=constants.TILE_SCALING, use_spatial_hash=True)

        jane = arcade.Sprite('penguin/game/assets/graphics/janePenguin.png', .25)
        cierra = arcade.Sprite('penguin/game/assets/graphics/cierraPenguin.png', .25)
        jacob = arcade.Sprite('penguin/game/assets/graphics/jacobPenguin.png', .25)
        benjamin = arcade.Sprite('penguin/game/assets/graphics/benjaminPenguin.png', .25)

        jane.center_x = 507
        jane.center_y = 381

        cierra.center_x = 2075
        cierra.center_y = 266

        jacob.center_x = 522
        jacob.center_y = 1076

        benjamin.center_x = 1311
        benjamin.center_y = 764

        room.wall_list.append(jane)
        room.wall_list.append(cierra)
        room.wall_list.append(jacob)
        room.wall_list.append(benjamin)

        return room


    def setupBoss(self):
        pass
