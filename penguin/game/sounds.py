import arcade
import pyglet
# This file is in charge of playing sounds. We need to give it access to the sound files. Pass in the sound to be played, and play it.

class Sounds:
    
    def __init__(self):
        """This class holds all of the sounds that we are going to be using, including sound effects
           and songs for various parts of the game"""
        self.volume = 20
        self.current_sound = None
        self.player = None
        self.sounds = {"main_theme":"penguin/game/assets/sounds/CrystalCaverns.wav", 
                        "intro_screen":"penguin/game/assets/sounds/CrystalCaverns.wav", 
                       "village_theme":"penguin/game/assets/sounds/SleighRide.wav",
                       "cave_theme": "penguin/game/assets/sounds/Cave.wav",
                       "boss_theme":"penguin/game/assets/sounds/IceBlizzard.wav",
                       "maze_theme": "penguin/game/assets/sounds/Maze.wav",
                       "end_screen":"penguin/game/assets/sounds/IceCream.wav",
                       "penguin-hit":"penguin/game/assets/sounds/hit.wav",
                       "boss-hit":"penguin/game/assets/sounds/PSnowball.wav",
                       "boss-death":"penguin/game/assets/sounds/roar.wav",
                       "player-death":"penguin/game/assets/sounds/recharage.wav",
                       "player-hit":"penguin/game/assets/sounds/snowballimpact.wav",
                       "zip-sound":"penguin/game/assets/sounds/mixkit-fast-magic-game-spell-883.wav"}
    
    def play_sound(self, sound):
        self.current_sound = sound
        self.player = arcade.Sound(self.sounds[sound]).play(volume=self.volume)

    def stop_sound(self, sound):
        self.current_sound = None
        arcade.Sound(self.sounds[sound]).stop(self.player)

    def get_current_sound(self):
        return self.current_sound
        
