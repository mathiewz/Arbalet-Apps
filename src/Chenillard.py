import random

from arbalet.colors import hsv_to_rgb
from arbalet.core import Arbalet
from arbaletApp import ArbaletApp


class Chenillard(ArbaletApp):
    x = 0
    y = 0

    #Fait un chenillard qui change de couleur pendant qu'il se balade
    def loop(self, arbalet: Arbalet):
        color = hsv_to_rgb(self.x * 1.0 / arbalet.width, 1, 1)
        arbalet.user_model.set_pixel(self.y, self.x, color)
        self.x += 1
        if self.x == arbalet.width:
            self.x = 0
            self.y = (self.y + 1) % arbalet.height


Chenillard().start()
