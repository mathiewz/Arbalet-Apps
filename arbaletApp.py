import argparse

import pygame
from arbalet.core import Rate, Application, Arbalet

LEFT = (-1, 0)
RIGHT = (1, 0)
DOWN = (0, 1)
UP = (0, -1)
NONE = (0, 0)
color = None

class ArbaletApp(Application):

    direction = UP

    def __init__(self):
        parser = argparse.ArgumentParser(description='Arbalet application')
        parser.add_argument('-col', '--color',
                            type=str,
                            default='red',
                            help='Color of the pixel (string of a HTML color)')
        parser.add_argument('-sp', '--speed',
                            type=int,
                            default=5,
                            help='speed of the loop')

        Application.__init__(self, parser,
                             touch_mode="quadridirectional")  # The argparse object is passed to class Application here

    def run(self):
        self.color = self.args.color
        speed = self.args.speed
        print("Starting args")
        print("=============")
        print("Height   :", self.arbalet.height)
        print("Width    :", self.arbalet.width)
        print("Speed    :", speed)
        print("Color    :", self.color)
        print("Hardware :", self.args.hardware)
        print("=============")
        print("Application started")

        # Then we display the actual worm
        rate = Rate(speed)
        while True:
            self.arbalet.user_model.set_all('black')
            self.process_events()
            self.loop(self.arbalet)
            rate.sleep()

    def process_events(self):
        new_dir = None
        for event in self.arbalet.events.get():
            # Joystick control
            if event.type == pygame.JOYHATMOTION:
                if event.value[1] == 1 and self.DIRECTION != DOWN:
                    new_dir = UP
                elif event.value[1] == -1 and self.DIRECTION != UP:
                    new_dir = DOWN
                elif event.value[1] == 0:
                    pass
                if event.value[0] == 1 and self.DIRECTION != LEFT:
                    new_dir = RIGHT
                elif event.value[0] == -1 and self.DIRECTION != RIGHT:
                    new_dir = LEFT
                elif event.value[0] == 0:
                    pass
            # Keyboard control
            elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                if event.key == pygame.K_UP:
                    new_dir = UP
                elif event.key == pygame.K_DOWN:
                    new_dir = DOWN
                elif event.key == pygame.K_RIGHT:
                    new_dir = RIGHT
                elif event.key == pygame.K_LEFT:
                    new_dir = LEFT

        for event in self.arbalet.touch.get():
            if event['key'] == 'up':
                new_dir = UP
            elif event['key'] == 'down':
                new_dir = DOWN
            elif event['key'] == 'right':
                new_dir = RIGHT
            elif event['key'] == 'left':
                new_dir = LEFT

        if new_dir is not None:
            self.direction = new_dir
        else:
            self.direction = NONE

    def loop(self, arbalet: Arbalet):
        print("No implementation found")
