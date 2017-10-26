# Arbalet-Apps
Several animations built with the [arbalet API](https://github.com/arbalet-project/arbasdk)

## How to use it
Every py file is executable, except arbaletApp that should do nothing.
Each file is an implementation on Arbalet App and can be launched with the same parameters as described in the API documentation.
Two more parameters are add : 
* -sp (or --speed) + a number to set the speed of the animation (default is 5) 
* -col (or --color) + a string to set a color usable in the implementations of the ArbaletApp class (with `self.color`)

 ## How to create new animations
 just create a new implementation of the class ArbaletApp and override the method `loop(self, arbalet: Arbalet)`
 This method is called in an infinite loop doing a clean of the board (all tiles are set black) and setting `selt.direction` before calling `loop(self, arbalet: Arbalet)`
