from cmu_graphics import *



# water
Rect(0, 125, 400, 150, fill='cornflowerBlue')

# grass and bushes
Rect(0, 0, 400, 125, fill='lawnGreen')
Rect(0, 275, 400, 125, fill='lawnGreen')
Oval(170, 0, 400, 120, fill='greenYellow')
Oval(330, -10, 300, 190, fill='springGreen')
Oval(40, 400, 380, 130, fill='paleGreen')
Oval(310, 410, 280, 190, fill='springGreen')

def drawFlower(x, y):
    Oval(x, y, 15, 30, fill='dodgerBlue')
    Oval(x, y, 15, 30, fill='dodgerBlue', rotateAngle=60)
    Oval(x, y, 15, 30, fill='dodgerBlue', rotateAngle=120)
    Circle(x, y, 5, fill='yellow')

def onMousePress(mouseX, mouseY):
    # Draw a flower if we clicked in either of the grassy areas.
    ### Place Your Code Here ###
    if (mouseY >= 275 or mouseY <= 125):
        drawFlower(mouseX, mouseY)
    pass

cmu_graphics.run()