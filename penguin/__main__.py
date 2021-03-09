from game.director import Director
from game import constants

director = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

director.start_game()