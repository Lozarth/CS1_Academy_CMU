from cmu_graphics import *



s = Star(200, 200, 225, 5, fill=None)

def onMouseMove(mouseX, mouseY):
    # Draw an orange circle if the mouse is inside the star and a green circle
    # if it isn't.
    ### Place Your Code Here ###
    if (s.contains(mouseX, mouseY) == True):
        Circle(mouseX, mouseY, 5, fill = 'orange')
    else:
        Circle(mouseX, mouseY, 5, fill = 'mediumAquamarine')
    pass

cmu_graphics.run()