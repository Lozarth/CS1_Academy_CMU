from cmu_graphics import *



# Draws the computer and screen.
Rect(0, 0, 400, 400, border='dimGrey', borderWidth=40)

# Draw the text on the computer's screen.
### Place Your Code Here ###

Label('System Loading...', 140, 75, fill = 'lime', font = 'arial', size = 18)

Label('Accepting Inputs:', 135, 100, fill = 'lime', font = 'arial', size = 18)

Label('> python hello_world.py', 195, 140, fill = 'lime', font = 'montserrat', size = 20)

Label('Good Evening, Earth', 170, 200, fill = 'lime', font = 'orbitron', size = 18)
cmu_graphics.run()