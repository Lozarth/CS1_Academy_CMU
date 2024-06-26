from cmu_graphics import *



app.background = 'paleGreen'

track = Rect(200, 200, 360, 360, align='center')
innerGrass = Rect(200, 200, 260, 260, fill='paleGreen', align='center')
Rect(200, 200, 310, 310, fill=None, border='white', dashes=True, align='center')

message = Label('Dot Race!', 200, 200, size=25)

finishLine = Line(320, 200, 390, 200, fill='white', lineWidth=30)
Line(315, 200, 390, 200, fill='red', lineWidth=30, dashes=True)

purpleDot = Circle(45, 175, 15, fill='darkOrchid')
blueDot = Circle(45, 225, 15, fill='dodgerBlue')

def onKeyHold(keys):
    # While the race is still going, move the dots and check if the race ends.
    if (message.value == 'Dot Race!'):
        if ('up' in keys):
            purpleDot.centerY -= 10
        if ('down' in keys):
            purpleDot.centerY += 10
        if ('left' in keys):
            purpleDot.centerX -= 10
        if ('right' in keys):
            purpleDot.centerX += 10
        if ('w' in keys):
            blueDot.centerY -= 10
        if ('s' in keys):
            blueDot.centerY += 10
        if ('a' in keys):
            blueDot.centerX -= 10
        if ('d' in keys):
            blueDot.centerX += 10

    # Check if one of the dots wins and if so change the value of the message.
    # A dot wins if either it touches the finish line or the center of the
    # other dot is not on the track.
    ### (HINT: The innerGrass is not a part of the track so you also need to
    #          check if the dots are touching the innerGrass.)
    ### Place Your Code Here ###
        
    if (track.containsShape(purpleDot) == False):
        if (innerGrass.hits(purpleDot.centerX, purpleDot.centerY)):
            message.value = 'Blue dot won!'
        
    if (track.containsShape(blueDot) == False):
        if (innerGrass.hits(blueDot.centerX, blueDot.centerY)):
            message.value = 'Purple dot won!'


def onKeyPress(key):
    # Do not change this function! It is for testing purposes only!
    if (key == 'q'):
        message.value = 'Dot Race!'
        purpleDot.centerX = 350
        purpleDot.centerY = 165
        blueDot.centerX = 350
        blueDot.centerY = 240

cmu_graphics.run()