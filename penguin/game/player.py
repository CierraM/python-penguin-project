from game.handle_health import SpriteWithHealth
import arcade

class Player(SpriteWithHealth):
    def __init__(self, image, scale, health_y_position, text_y_position, text_x_position, font_largeness, health_width, height, max_health):
        super().__init__(image, scale, health_y_position, text_y_position, text_x_position, font_largeness, health_width, height, max_health)
        self.scale = scale
        self.textures = []
        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(image)
        self.textures.append(texture)
        texture = arcade.load_texture(image, flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = texture

    def update(self, change_x, change_y):
        TEXTURE_LEFT = 0
        TEXTURE_RIGHT = 1

        self.center_x += change_x
        self.center_y += change_y

        # Figure out if we should face left or right
        if change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]