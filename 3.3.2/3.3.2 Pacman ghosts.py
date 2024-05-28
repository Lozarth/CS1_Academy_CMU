from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill='midnightBlue')

# Parameters give the center of the white part of the eye.
def drawEye(eyeCenterX, eyeCenterY):
    Circle(eyeCenterX, eyeCenterY, 20, fill='white')
    Circle(eyeCenterX, eyeCenterY, 10, fill='cornflowerBlue', align='right')

# x is the centerX of the body, y is the centerY of all feet.
def drawFeet(x, y, color):
    Circle(x - 40, y, 20, fill=color)
    Circle(x + 40, y, 20, fill=color)
    Circle(x, y, 20, fill=color)

# centerX and centerY are the center of the body of the ghost.
def drawGhost(centerX, centerY, name, color):
    # body
    Rect(centerX, centerY, 120, 80, fill=color, align='center')

    # head
    Circle(centerX, centerY - 40, 60, fill=color)

    # Draw the eyes.
    ### Place Your Code Here ###
    
    # Left Scalera
    Circle(
        centerX - 25, centerY - 55,
        20,
        
        fill = 'white'
    )
    # Left Iris
    Circle(
        centerX - 35, centerY - 55,
        10,
        
        fill = 'cornflowerBlue'
    )
    # Right Scalera
    Circle(
        centerX + 20, centerY - 55,
        20,
        
        fill = 'white'
    )
    # Right Iris
    Circle(
        centerX + 10, centerY - 55,
        10,
        
        fill = 'cornflowerBlue'
    )
    # Draw the feet.
    ### Place Your Code Here ###
    Circle(
        centerX - 40, centerY + 40,
        20,
        
        fill = color
    )
    Circle(
        centerX, centerY + 40,
        20,
        
        fill = color
    )
    Circle(
        centerX + 40, centerY + 40,
        20,
        
        fill = color
    )

    # Create a label with the name of the ghost.
    ### Place Your Code Here ###
    Label(
        name,
        centerX, centerY + 70,
        
        fill = 'white',
        font = 'monospace',
        size = 25
    )

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawGhost(200, 200, 'Sue', 'violet')

cmu_graphics.run()