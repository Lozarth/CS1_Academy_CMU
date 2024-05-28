from cmu_graphics import *



# Draws the background and the stem.
Rect(0, 0, 400, 400, fill = 'skyBlue')
Rect(180, 325, 40, 80, fill = 'green')
Rect(215, 345, 50, 30, fill = 'green')

# Adjust the starts of these gradients to properly color the flower.
# Draws the top row of the flower.
### Modify Your Code Here ###
Rect(40, 80, 100, 75, fill = gradient('hotPink', 'indigo', start = 'top-left'))
Rect(150, 80, 100, 75, fill = gradient('hotPink', 'indigo', start = 'top'))
Rect(260, 80, 100, 75, fill = gradient('hotPink', 'indigo', start = 'top-right'))

# Draws the middle row of the flower.
### Modify Your Code Here ###
Rect(40, 165, 100, 75, fill = gradient('hotPink', 'indigo', start = 'left'))
Rect(150, 165, 100, 75, fill = gradient('hotPink', 'indigo'))
Rect(260, 165, 100, 75, fill = gradient('hotPink', 'indigo', start = 'right'))

# Draws the bottom row of the flower.
### Modify Your Code Here ###
Rect(40, 250, 100, 75, fill = gradient('hotPink', 'indigo', start = 'bottom-left'))
Rect(150, 250, 100, 75, fill = gradient('hotPink', 'indigo', start = 'bottom'))
Rect(260, 250, 100, 75, fill = gradient('hotPink', 'indigo', start = 'bottom-right'))

cmu_graphics.run()