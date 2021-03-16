from game import constants
import arcade


class SpriteWithHealth(arcade.Sprite):
    """Create a sprite with health points
    """

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        self.max_health = max_health
        self.cur_health = max_health
    
    def draw_health_number(self):
        """Draw how many hit points you have
        """
        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                        start_x = self.center_x + constants.HEALTH_NUMBER_OFFSET_X,
                        start_y = self.center_y + constants.HEALTH_NUMBER_OFFSET_Y,
                        font_size = 11,
                        color = arcade.color.RED)

    def draw_health_bar(self):
        """Draw the health bar
        """
        #Draw red bar portion
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x = self.center_x,
                                        center_y = self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                        width = constants.HEALTHBAR_WIDTH,
                                        height = 5,
                                        color = arcade.color.RED)
        #width based on health
        health_width = constants.HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x = self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                    center_y = self.center_y + 32,
                                    width = health_width,
                                    height = constants.HEALTHBAR_HEIGHT,
                                    color = arcade.color.GREEN)