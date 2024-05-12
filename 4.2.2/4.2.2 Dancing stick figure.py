app.background = gradient('azure', 'lightBlue', 'blue')

# face and body
Circle(200, 135, 25)
Line(200, 160, 200, 240)

# upper arms
leftArm = Line(200, 185, 150, 175)
rightArm = Line(200, 185, 250, 175)

# legs
Line(200, 240, 230, 300)
Line(200, 240, 170, 300)

def toggleLeftArm():
    # Move the left arm down if it is currently up, and up if it is currently down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if it is currently up, and up if it is currently down.
    ### Place Your Code Here ###
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125
    pass

def onKeyPress(key):
    # On left and right key press, call the corresponding helper function.
    ### Place Your Code Here ###
    if (key == 'left'):
        toggleLeftArm()
    elif (key == 'right'):
        toggleRightArm()
    pass
