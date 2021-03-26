import arcade
class Room:
    """This class is in charge of keeping track of information about a single room
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.width = 0
        self.height = 0
        self.size = None
        self.soundtrack = None
        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None