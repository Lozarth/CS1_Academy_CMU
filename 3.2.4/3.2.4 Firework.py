from cmu_graphics import *



# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # Check if the firework is high enough up to explode.
    ### Fix Your Code Here ###
    if (mouseY < 150):
        Star(mouseX, mouseY, 100, 12, fill=gradient('red', 'white'), roundness=10)
    
        Star(mouseX, mouseY, 100, 12, fill=gradient('yellow', 'white'), roundness=10, rotateAngle=10)

        Star(mouseX, mouseY, 100, 12, roundness=10, rotateAngle=5)

    # If the firework is not high enough, draw a rising pre-firework line.
    ### Place Your Code Here ###
    
    if (mouseY > 150):
        Line(
            mouseX, 400,
            mouseX, mouseY,
            
            fill = gradient('black', 'red', 'yellow', 'black', start = 'top')
        )

cmu_graphics.run()