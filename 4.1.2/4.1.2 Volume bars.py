from cmu_graphics import *



app.background = 'black'

leftVolumeBar = Line(75, 300, 75, 400, lineWidth=100, dashes=True,
                     fill=gradient('black', 'red', 'orange', 'yellow',
                                   'lawnGreen', start='top'))
centerVolumeBar = Line(200, 300, 200, 400, lineWidth=100, dashes=True,
                       fill=gradient('black', 'red', 'orange', 'yellow',
                                     'lawnGreen', start='top'))
rightVolumeBar = Line(325, 300, 325, 400, lineWidth=100, dashes=True,
                      fill=gradient('black', 'red', 'orange', 'yellow',
                                    'lawnGreen', start='top'))

def setVolumeBars(newLeftBarY1, newCenterBarY1, newRightBarY1):
    # Set each volume bar to new y1 value.
    leftVolumeBar.y1 = newLeftBarY1
    centerVolumeBar.y1 = newCenterBarY1
    rightVolumeBar.y1 = newRightBarY1

def onMouseMove(mouseX, mouseY):
    # Change the height of volume bars based on which volume bar the mouse is above.
    ### (HINT: The volume bars are set at either a height of mouseY or
    #          400 - mouseY.)
    ### Place Your Code Here ###
    if (mouseX < 125):  
        leftVolumeBar.y1   = mouseY
        centerVolumeBar.y1 = 400 - mouseY
        rightVolumeBar.y1  = 400 - mouseY
    elif (mouseX >= 125 and mouseX < 275):
        leftVolumeBar.y1   = 400 - mouseY
        centerVolumeBar.y1 = mouseY
        rightVolumeBar.y1  = 400 - mouseY
    elif (mouseX >= 275):
        leftVolumeBar.y1   = 400 - mouseY
        centerVolumeBar.y1 = 400 - mouseY        
        rightVolumeBar.y1  = mouseY

    pass

cmu_graphics.run()