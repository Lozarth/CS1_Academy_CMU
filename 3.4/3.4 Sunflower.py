app.background = gradient('powderBlue', 'aliceBlue', start='top')

sun = Circle(200, 0, 70,  fill='gold')

# stem and leaves
Oval(170, 340, 25, 55, fill=gradient('yellowGreen', 'green', start='top'),
     rotateAngle=-45)
Oval(232, 300, 25, 55, fill=gradient('yellowGreen', 'green', start='top'),
     rotateAngle=45)
Line(200, 400, 200, 220, fill=gradient('yellowGreen', 'green', start='top'),
     lineWidth=25)

flower = Star(200, 220, 110, 14, fill=gradient('yellow', 'goldenrod'), roundness=80)
flower.height = 150

flowerCenter = Oval(200, 220, 115, 85, fill=gradient('chocolate', 'saddleBrown'))

def onMouseMove(mouseX, mouseY):
    # Move the sun to match the mouse's x value.
    sun.centerX = mouseX

    # Rotate the flower and its center to point towards the sun.
    ### (HINT: Use the inspector to figure out what these angles should be!)
    ### Place Your Code Here ###
    if (mouseX > 200):
        flower.rotateAngle = 45
        flowerCenter.rotateAngle = 45
    else:
        flower.rotateAngle = -45
        flowerCenter.rotateAngle = -45
