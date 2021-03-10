import arcade
# This file is in charge of playing sounds. We need to give it access to the sound files. Pass in the sound to be played, and play it.

class Sounds:
    
    def __init__(self):
        """This class holds all of the sounds that we are going to be using, including sound effects
           and songs for various parts of the game"""
        self.volume = 30
        self.sounds = {"main_1":"penguin/game/assets/sounds/CrystalCaverns.wav", 
                       "main_2":"penguin/game/assets/sounds/SleighRide.wav",
                       "boss":"penguin/game/assets/sounds/IceBlizzard.wav",
                       "end":"penguin/game/assets/sounds/IceCream.wav"}
    
    def play_sound(self, sound):
        self.sounds[sound].play(volume=self.volume)
