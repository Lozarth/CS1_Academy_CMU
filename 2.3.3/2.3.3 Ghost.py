Rect(0, 0, 400, 400,
     fill=gradient(rgb(10, 10, 70), 'midnightBlue', start='bottom'))
Rect(0, 325, 400, 75,
     fill=gradient(rgb(70, 35, 10), rgb(100, 45, 15), start='bottom'))

ghost = Polygon(150, 150, 150, 275, 175, 250, 200, 275, 225, 250,
                250, 275, 250, 150, 240, 130, 210, 110, 190, 110, 160, 130,
                fill='white')

# eyes
Circle(190, 150, 5)
Circle(210, 150, 5)

flashlightBeam = Circle(200, 200, 170, fill='yellow', opacity=20)

ghost.opacity = 5
flashlightBeam.visible = False

def onMousePress(mouseX, mouseY):
    # Turn on the flashlight.
    ### Place Your Code Here ###
    flashlightBeam.visible = True
    pass

    # Make the ghost more visible.
    ### Place Your Code Here ###
    ghost.opacity =  80
    
def onMouseRelease(mouseX, mouseY):
    # Turn off the flashlight.
    ### Place Your Code Here ###
    flashlightBeam.visible = False
    pass

    # Make the ghost fade into the wall.
    ### Place Your Code Here ###
    ghost.opacity = 5
