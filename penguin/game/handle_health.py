from game import constants
import arcade


class SpriteWithHealth(arcade.Sprite):
    """Create a sprite with health points
    """

    def __init__(self, image, scale, health_y_position, text_y_position, text_x_position, font_largeness, health_width, height, max_health):
        super().__init__(image, scale)

        
        self.max_health = max_health
        self.cur_health = max_health
        self.health_bar_y = health_y_position
        self.health_number_y_position = text_y_position
        self.health_number_x_position = text_x_position
        self.font = font_largeness
        self.health_bar_width = health_width
        self.health_bar_height = height
    
    def draw_health_number(self):
        """Draw how many hit points you have
        """
        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                        start_x = self.center_x + self.health_number_x_position,
                        start_y = self.center_y + self.health_number_y_position,
                        font_size = self.font,
                        color = arcade.color.BLACK)

    def draw_health_bar(self):
        """Draw the health bar
        """
        #Draw red bar portion
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x = self.center_x,
                                        center_y = self.center_y + self.health_bar_y,
                                        width = self.health_bar_width,
                                        height = 5,
                                        color = arcade.color.RED)
        #width based on health
        health_width = self.health_bar_width * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x = self.center_x - 0.5 * (self.health_bar_width - health_width),
                                    center_y = self.center_y + self.health_bar_y,
                                    width = health_width,
                                    height = self.health_bar_height,
                                    color = arcade.color.GREEN)