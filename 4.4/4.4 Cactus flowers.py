app.background = gradient('dodgerBlue', 'deepSkyBlue', 'lightCyan', start='top')

cactusTop1 = Circle(200, 50, 40, fill='forestGreen', border='wheat', dashes=(5, 6))
cactusTop2 = Circle(200, 50, 25, fill='green', border='wheat', dashes=(4, 5))
cactusTop3 = Circle(200, 50, 10, fill='darkGreen', border='wheat', dashes=(3, 5))
cactus1 = Rect(160, 50, 80, 350, fill='forestGreen', border='wheat', dashes=(5, 6))
cactus2 = Rect(175, 50, 50, 350, fill='green', border='wheat', dashes=(4, 5))
cactus3 = Rect(190, 50, 20, 350, fill='darkGreen', border='wheat', dashes=(3, 5))
sand = Oval(200, 440, 500, 160, fill='darkKhaki')

def drawCactusArm(x, y):
    # Makes the top of the arm rounded.
    Circle(x, y - 40, 15, fill='green', border='wheat', dashes=(2, 5))
    Circle(x, y - 40, 8, fill='darkGreen', border='wheat', dashes=(4, 6))

    # Makes the elbow of the arm rounded.
    Circle(x, y, 15, fill='green', border='wheat', dashes=(2, 5))
    Circle(x, y, 7, fill='darkGreen', border='wheat', dashes=(4, 6))

    # Draws the horizontal part of the arm. Notice the alignment!
    if (x < 200):
        Rect(x + 5, y, 200 - x, 30, fill='green', border='wheat', dashes=(2, 5),
             align='left')
        Rect(x + 5, y, 200 - x, 14, fill='darkGreen', border='wheat',
             dashes=(4, 6), align='left')
    elif (x > 200):
        Rect(x - 5, y, x - 200, 30, fill='green', border='wheat', dashes=(2, 5),
             align='right')
        Rect(x - 5, y, x - 200, 14, fill='darkGreen', border='wheat',
             dashes=(4, 6), align='right')

    # Draws the vertical part of the arm.
    Rect(x - 15, y - 40, 30, 35, fill='green', border='wheat', dashes=(2, 5))
    Rect(x - 7, y - 40, 16, 35, fill='darkGreen', border='wheat', dashes=(4, 6))

def drawCactusFlower(x, y):
    # Here (x, y) is the center of the middle flower petal, 60 pixels above
    # the arm's elbow.
    Oval(x - 10, y, 12, 20, fill='hotPink', rotateAngle=-20)
    Oval(x + 10, y, 12, 20, fill='hotPink', rotateAngle=20)
    Oval(x, y, 15, 25, fill='purple')

def onMousePress(mouseX, mouseY):
    # Add a cactus arm and flower.
    # Make sure the cactus and sand is in front of the added arms.
    ### Place Your Code Here ###
    drawCactusArm(mouseX, mouseY)
    drawCactusFlower(mouseX, mouseY - 60)
    cactusTop1.toFront()
    cactusTop2.toFront()
    cactusTop3.toFront()
    cactus1.toFront()
    cactus2.toFront()
    cactus3.toFront()
    sand.toFront()
    pass
