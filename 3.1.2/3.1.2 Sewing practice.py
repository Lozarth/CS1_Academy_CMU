from cmu_graphics import *



app.background = 'tan'

# piece of fabric
Rect(50, 100, 300, 200, fill='navy')
Line(50, 200, 350, 200, fill='blue', lineWidth=200, opacity=10, dashes=(4, 3))
Line(200, 100, 200, 300, fill='steelBlue', lineWidth=300, opacity=10,
     dashes=(3, 4))

newStitch = Line(0, 0, 0, 0, fill='lightBlue', dashes=True)

def onMousePress(mouseX, mouseY):
    newStitch.visible = True
    newStitch.x1 = mouseX
    newStitch.y1 = mouseY
    newStitch.x2 = mouseX
    newStitch.y2 = mouseY

def onMouseDrag(mouseX, mouseY):
    # Move the stitch to follow the mouse.
    ### Place Your Code Here ###
    newStitch.x2 = mouseX
    newStitch.y2 = mouseY
    pass

def onMouseRelease(mouseX, mouseY):
    # Draw a new line where the new stitch is, and hide the new stitch.
    ### Place Your Code Here ###
    newStitch.visible = False
    Line(
        newStitch.x1,
        newStitch.y1,
        newStitch.x2,
        newStitch.y2,
        
        fill = 'dodgerBlue',
        dashes = True
    )
    pass

cmu_graphics.run()