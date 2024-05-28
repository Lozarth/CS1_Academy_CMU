from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill=rgb(230, 230, 255))

# Draw the cup.
### Place Your Code Here ###

Polygon(
    105, 90,
    295, 90,
    275, 355,
    125, 355,
    
    fill = 'ivory'
)

# Draw the bubbles.
### (HINT: We have bubbles in two different colors.)
### Place Your Code Here ###

Circle(
    160, 325,
    15,
    
    fill = 'sienna'
)

Circle(
    190, 280,
    15,
    
    fill = 'chocolate'
)

Circle(
    210, 320,
    15,
    
    fill = 'chocolate'
)

Circle(
    245, 300,
    15,
    
    fill = 'sienna'
)

# Now draw the tea inside the cup using two shapes.
### Place Your Code Here ###

Polygon(
    117, 120,
    283, 120,
    266, 345,
    134, 345,
    
    fill = 'mediumPurple',
    opacity = 70
)

Oval(
    200, 120,
    165, 30,
    
    fill = 'mediumPurple'
)

# Finally, draw the lid and the straw!
### (HINT: Pay attention to the order of shapes.)
### Place Your Code Here ###

Oval(
    200, 90,
    205, 50,
    
    fill = 'dimGray'
)

Line(
    200, 40,
    200, 90,
    
    fill = 'skyBlue',
    lineWidth = 30
)
cmu_graphics.run()