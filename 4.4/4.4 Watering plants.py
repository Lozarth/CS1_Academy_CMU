from cmu_graphics import *



app.background = gradient('darkSlateGrey', 'deepSkyBlue', start='top')

# grass
Rect(0, 360, 400, 360, fill='darkOliveGreen')

water = Polygon(200, 35, 190, 55, 190, 60,
                200, 66, 210, 60, 210, 55, fill='lightSkyBlue')

leftStem = Line(85, 365, 85, 320, fill='lightGreen', lineWidth=5)
leftPot = Polygon(55, 345, 115, 345, 105, 400, 65, 400, fill='saddleBrown')

rightStem = Line(315, 365, 315, 320, fill='darkGreen', lineWidth=5)
rightPot = Polygon(345, 345, 285, 345, 295, 400, 335, 400, fill='saddleBrown')

def growLeftFlower():
    # Either grow some leaves on the stem or grow a flower.
    if (leftStem.y2 > 225):
        Oval(leftStem.x2, leftStem.y2, 20, 10, fill='lightGreen',
             rotateAngle=30, align='right')
        Oval(leftStem.x2, leftStem.y2, 20, 10, fill='lightGreen',
             rotateAngle=-30, align='left')
        leftStem.y2 -= 30
    else:
        Star(leftStem.x2, leftStem.y2 - 20, 35, 7, fill='pink')
        Circle(leftStem.x2, leftStem.y2 - 20, 10, fill='lemonChiffon')

def growRightFlower():
    # Either grow some leaves on the stem or grow a flower.
    if (rightStem.y2 > 175):
        Oval(rightStem.x2, rightStem.y2, 20, 10, fill='darkGreen',
             rotateAngle=30, align='right')
        Oval(rightStem.x2, rightStem.y2, 20, 10, fill='darkGreen',
             rotateAngle=-30, align='left')
        rightStem.y2 -= 30
    else:
        Star(rightStem.x2, rightStem.y2 - 20, 35, 7, fill='mediumVioletRed')
        Circle(rightStem.x2, rightStem.y2 - 20, 10, fill='gold')

def onMousePress(mouseX, mouseY):
    # Grow the plant that is watered.
    ### (HINT: A plant can be watered either on the stem or in the pot.)
    ### Place Your Code Here ###
    if (water.hitsShape(leftStem) or water.hitsShape(leftPot)):
        growLeftFlower()
    elif (water.hitsShape(rightStem) or water.hitsShape(rightPot)):
        growRightFlower()
    pass

def onMouseMove(mouseX, mouseY):
    water.centerX = mouseX
    water.centerY = mouseY

cmu_graphics.run()