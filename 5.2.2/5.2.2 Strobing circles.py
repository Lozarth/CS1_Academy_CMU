from cmu_graphics import *



app.background = 'azure'

head = Circle(200, 200, 30, fill='mediumOrchid')

def getNewHeadColor():
    # Cycle through the three colors.
    if (head.fill == 'mediumOrchid'):
        head.fill = 'mediumSpringGreen'
    elif (head.fill == 'mediumSpringGreen'):
        head.fill = 'blue'
    else:
        head.fill = 'mediumOrchid'

def onKeyHold(keys):
    # Depending on the keys held down, move the head in an appropriate direction.
    ### Place Your Code Here ###
    if ('up' in keys):
        head.centerY -= 10
    if ('down' in keys):
        head.centerY += 10
    if ('left' in keys):
        head.centerX -= 10
    if ('right' in keys):
        head.centerX += 10
    # Draw a new circle where the head is with the same fill.
    ### Place Your Code Here ###
    Circle(head.centerX, head.centerY, head.radius, fill = head.fill)
    # Change the color of the head.
    ### Place Your Code Here ###
    getNewHeadColor()
    pass

cmu_graphics.run()