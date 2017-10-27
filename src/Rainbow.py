from arbalet.colors import hsv_to_rgb
from arbalet.core import Arbalet
from arbaletApp import ArbaletApp


class MyApp(ArbaletApp):
    delta = 0

    # Modifie la couleur selon la diagonale du mur de pixel
    def loop(self, arbalet: Arbalet):
        coordX = 0
        coordY = 0
        for i in range(arbalet.width + arbalet.height):
            coordX = i
            coordY = 0
            color = hsv_to_rgb(((coordX * 1.0 / arbalet.width) + self.delta) % 1, 1, 1)
            for j in range(i+1):
                if coordY < arbalet.height and coordX < arbalet.width:
                    arbalet.user_model.set_pixel(coordY, coordX, color)
                coordX -= 1
                coordY += 1
        self.delta = (self.delta + 1.0 / arbalet.width) % 1


MyApp().start()
