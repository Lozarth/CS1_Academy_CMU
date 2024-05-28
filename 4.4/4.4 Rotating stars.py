from cmu_graphics import *



app.background = gradient('azure', 'lavenderBlush', start='top')

s1 = Star(200, 125, 25, 5, fill=None, border='skyBlue', borderWidth=10)
s2 = Star(275, 250, 25, 5, fill=None, border='crimson', borderWidth=10)
s3 = Star(125, 250, 25, 5, fill=None, border='gold', borderWidth=10)

# Indicate size is growing.
s1.isGrowing = True
s2.isGrowing = True
s3.isGrowing = True

def rotateAndResizeStar(s):
    # When the star is growing, increase the radius and rotate it clockwise.
    # Otherwise, decrease the radius and rotate it counter-clockwise.
    ### (HINT: Look at the onMouseMove function. This helper function is called
    #          from there three times, once with each of the three stars!)
    ### Place Your Code Here ###
    if (s.isGrowing):
        s.radius += 5
        s.rotateAngle += 5
    else:
        s.radius -= 5
        s.rotateAngle -= 5
    # When the radius of the star is at most 5 or at least 200, change the
    # custom property appropriately.
    ### Place Your Code Here ###
    if (s.radius <= 5):
        s.isGrowing = True
    elif (s.radius >= 200):
        s.isGrowing = False
    pass

def onMouseMove(mouseX, mouseY):
    rotateAndResizeStar(s1)
    rotateAndResizeStar(s2)
    rotateAndResizeStar(s3)

def onKeyPress(key):
    # This is for testing purposes - DO NOT change this function.
    if (key == 'a'):
        s1.radius = 195
        s2.radius = 195
        s3.radius = 195
    if (key == 'b'):
        s1.radius = 10
        s2.radius = 10
        s3.radius = 10

cmu_graphics.run()