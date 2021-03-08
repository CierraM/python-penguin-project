import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]

        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()

        # handle ball / paddle collision
        if paddle.collision(ball):
            ball.set_velocity(ball.get_velocity().reverse_y())

        # handle ball / wall collision
        elif ball_x <= 1 or ball_x >= constants.MAX_X - 1:
            ball.set_velocity(ball.get_velocity().reverse_x())

        # handle ball / ceiling collision
        elif ball_y <= 1:
            ball.set_velocity(ball.get_velocity().reverse_y())

        # handle ball / floor collision
        elif ball_y >= constants.MAX_Y -1:
            # remove ball from game by hiding it
            cast["ball"][0].set_velocity(Point(0,0)) 
            cast["ball"][0].set_text("")
            # pass

        # handle ball / brick collisions
        else:
            for brick in bricks:
                if ball.collision(brick):
                    bricks.remove(brick)
                    ball.set_velocity(ball.get_velocity().reverse_y())
