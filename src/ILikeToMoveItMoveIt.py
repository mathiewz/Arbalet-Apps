import random

from arbalet.colors import hsv_to_rgb
from arbalet.core import Arbalet
from arbaletApp import ArbaletApp


class ILikeToMoveItMoveIt(ArbaletApp):
    x = 0
    y = 0

    #Permet d'utiliser les commandes directionelles
    def loop(self, arbalet: Arbalet):
        self.x = (self.x + self.direction[0]) % arbalet.width
        self.y = (self.y + self.direction[1]) % arbalet.height
        arbalet.user_model.set_pixel(self.y, self.x, self.color)

ILikeToMoveItMoveIt().start()
