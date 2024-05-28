from cmu_graphics import *

app.background = 'black'

s1 = Circle(200, 200, 150, fill=None, border='lightCyan', borderWidth=16)
s1.isGrowing = True

s2 = RegularPolygon(200, 200, 134, 6, fill=None, border='lightCyan', borderWidth=12)
s2.isGrowing = True

s3 = RegularPolygon(200, 200, 105, 6, fill=None, rotateAngle=30, border='lightCyan', borderWidth=12)
s3.isGrowing = True

s4 = Star(200, 200, 80, 6, fill=None, border='lightCyan', borderWidth=10)
s4.isGrowing = True

def rotateAndResizeShape(s):
    s.rotateAngle += 2

    # When the shape is growing, increase the radius and borderWidth. Otherwise,
    # decrease each accordingly.
    ### Place Your Code Here ###
    if (s.isGrowing):
        s.radius += 2
        s.borderWidth += .1
    else:
        s.radius -= 2
        s.borderWidth -= .1
        
    # When the radius of the shape is less than 5 or more 200, change the
    # custom property appropriately.
    ### Place Your Code Here ###
    if (s.radius < 5):
        s.isGrowing = True
    elif (s.radius > 200):
        s.isGrowing = False

def onMouseMove(mouseX, mouseY):
    # Rotate and resize all four shapes.
    ### Place Your Code Here ###
    rotateAndResizeShape(s1)
    rotateAndResizeShape(s2)
    rotateAndResizeShape(s3)
    rotateAndResizeShape(s4)

cmu_graphics.run()