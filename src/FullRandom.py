import random

from arbalet.core import Arbalet
from arbaletApp import ArbaletApp


class FullRandom(ArbaletApp):

    #Affiche une couleur random sur chaque case (raffraichit a chaque boucle)
    def loop(self, arbalet: Arbalet):
        for i in range(arbalet.height):
            for j in range(arbalet.width):
                color = (random.random(), random.random(), random.random())
                arbalet.user_model.set_pixel(i, j, color)


FullRandom().start()
