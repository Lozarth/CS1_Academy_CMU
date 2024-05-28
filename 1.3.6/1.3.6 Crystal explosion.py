from cmu_graphics import *



# Draws the background.
Rect(0, 0, 400, 400)

# Draw a bunch of stars to create the crystal.
### (HINT: The Inspector results are ordered in a particular fashion!)
### Place Your Code Here ###

Star(200, 200, 200, 13, fill = None, roundness = 10, border = 'aliceBlue', dashes=True)
Star(200, 200, 150, 11, fill = None, roundness = 20, border = 'aliceBlue', dashes=True)
Star(200, 200, 100, 7, fill = None, roundness = 5, border = 'aliceBlue', dashes=True)
Star(200, 200, 50, 19, fill = None, roundness = 50, border = 'aliceBlue', dashes=True)

cmu_graphics.run()