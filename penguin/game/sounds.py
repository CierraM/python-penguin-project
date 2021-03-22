import arcade
# This file is in charge of playing sounds. We need to give it access to the sound files. Pass in the sound to be played, and play it.

class Sounds:
    
    def __init__(self):
        """This class holds all of the sounds that we are going to be using, including sound effects
           and songs for various parts of the game"""
        self.volume = 20
        self.sounds = {"main_1":"penguin/game/assets/sounds/CrystalCaverns.wav", 
                       "main_2":"penguin/game/assets/sounds/SleighRide.wav",
                       "boss":"penguin/game/assets/sounds/IceBlizzard.wav",
                       "end":"penguin/game/assets/sounds/IceCream.wav",
                       "penguin-hit":"penguin/game/assets/sounds/hit.wav",
                       "boss-hit":"penguin/game/assets/sounds/pop.wav",
                       "boss-death":"penguin/game/assets/sounds/roar.wav",
                       "player-death":"penguin/game/assets/sounds/recharage.wav",
                       "player-hit":"penguin/game/assets/sounds/sweep.wav"}
    
    def play_sound(self, sound):
        arcade.Sound(self.sounds[sound]).play(volume=self.volume)
        
