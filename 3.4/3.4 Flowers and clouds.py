from cmu_graphics import *



app.background = gradient('deepSkyBlue', 'lightCyan', start='top')

# ground
Rect(0, 255, 400, 145, fill='oliveDrab')
Oval(200, 255, 400, 20, fill='oliveDrab')

def drawCloud(x, y, color):
    # Draws a cloud with the given color and center at (x, y).
    Oval(x, y, 100, 45, fill=color)
    Circle(x + 40, y - 10, 20, fill=color)
    Circle(x + 10, y - 20, 30, fill=color)
    Circle(x - 15, y - 20, 30, fill=color)
    Circle(x - 30, y, 20, fill=color)

def drawFlower(x, y):
    # Draws a flower centered at (x, y-10) when it is called.
    Oval(x, y - 10, 10, 20, fill='deepPink')
    Oval(x, y - 10, 10, 20, fill='hotPink', rotateAngle=60)
    Oval(x, y - 10, 10, 20, fill='deepPink', rotateAngle=120)
    Circle(x, y - 10, 2, fill='yellow')

def onMousePress(mouseX, mouseY):
    # When the mouseY is less than 255, draw a cloud with an rgb value that
    # depends on mouseY. When the mouseY is at least 255, draw a flower.
    ### Place Your Code Here ###
    if (mouseY < 255):
        drawCloud(mouseX, mouseY, rgb(mouseY, mouseY, mouseY))
    elif (mouseY >= 255):
        drawFlower(mouseX, mouseY)
    pass

cmu_graphics.run()