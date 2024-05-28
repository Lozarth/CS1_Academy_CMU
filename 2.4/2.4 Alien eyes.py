from cmu_graphics import *



app.background = gradient('black', 'midnightBlue', start='top')

# Draw the alien body.
### (Hint: Use 7 shapes.)
### Place Your Code Here ###

# Torso
Circle(
    200, 200,
    100,
    
    fill = 'limeGreen'
)

# Left Arm
Circle(
    100, 200,
    20,
    
    fill = 'limeGreen'
)

# Right Arm
Circle(
    300, 200,
    20,
    
    fill = 'limeGreen'
)

# Left Leg
Circle(
    150, 290,
    20,
    
    fill = 'limeGreen'
)

# Right Leg
Circle(
    250, 290,
    20,
    
    fill = 'limeGreen'
)

# Mouth
Circle(
    200, 245,
    25
)
# Overlay
Rect(
    175, 220,
    50,
    25,
    
    fill = 'limeGreen'
)

# Write a function that draws one eye.
def drawEye(centerX, centerY, eyeSize, pupilSize):
    ### Place Your Code Here ###
    Circle(
        centerX, centerY,
        eyeSize,
        
        fill = 'white'
    )
    
    Circle(
        centerX, centerY,
        pupilSize,
        
        fill = 'black'
    )
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawEye(200, 175, 55, 27)

cmu_graphics.run()