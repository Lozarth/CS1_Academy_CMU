from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill='skyBlue')

# Draws the cup and a few fries.


Polygon(80, 200, 120, 400, 280, 400, 320, 200, fill='red')
Oval(200, 200, 240, 60, fill='gold', border='gold', borderWidth=10)
Line(140, 80, 160, 200, fill=gradient('yellow', 'gold', start='top'), lineWidth=25)
Line(260, 80, 240, 200, fill=gradient('yellow', 'gold', start='top'), lineWidth=25)

# Draw the rest of the fries.
### Place Your Code Here ###

Line(
    80, 80,
    120, 200,
    
    fill = gradient('yellow', 'gold', start = 'top'),
    lineWidth = 25
)

Line(
    200, 80,
    200, 200,
    
    fill = gradient('yellow', 'gold', start = 'top'),
    lineWidth = 25
)

Line(
    320, 80,
    280, 200,
    
    fill = gradient('yellow', 'gold', start = 'top'),
    lineWidth = 25
)

# Draw the McDonald's logo.
### (HINT: The logo consists of two ovals and another shape to cover up the
#          bottom.)
### Place Your Code Here ###

Oval(
    180, 400,
    50, 300,
    
    fill = None,
    
    border = 'gold',
    borderWidth = 10
)

Oval(
    220, 400,
    50, 300,
    
    fill = None,
    
    border = 'gold',
    borderWidth = 10
)

Polygon(
    120, 340,
    280, 340,
    280, 400,
    120, 400,
    
    fill = 'red'
)

# Make the McDonald's cup curved at the bottom.
### (HINT: One shape is needed to achieve this!)
### Place Your Code Here ###

Oval(
    200, 400,
    160, 40,
    
    fill = 'skyBlue',
    
    border = 'gold',
    borderWidth = 10
)

# Draw the label at the top.
### Place Your Code Here ###

Rect(
    120, 20,
    160, 40,
    
    fill = 'red'
)

Label(
    'im lovin it',
    200, 40,
    
    fill = 'gold',
    font = 'arial',
    size = 25,
    bold = True
)
cmu_graphics.run()