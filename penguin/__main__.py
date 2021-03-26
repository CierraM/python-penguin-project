from game.director import IntroView
from game import constants
import arcade


window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
window.set_update_rate(1/30)
start_view = IntroView()
window.show_view(start_view)
arcade.run()

# director = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

# director.start_game()