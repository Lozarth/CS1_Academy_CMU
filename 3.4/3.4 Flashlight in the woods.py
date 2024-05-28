from cmu_graphics import *



app.background = gradient('black', 'midnightBlue')

# hills
Polygon(0, 400, 0, 235, 280, 210, 400, 230, 400, 400, fill=rgb(0, 60, 0))
Polygon(0, 275, 170, 285, 400, 260, 400, 400, 0, 400, fill='darkOliveGreen')
Polygon(0, 400, 0, 330, 240, 310, 400, 325, 400, 400, fill='olive')

def drawTree(x, y):
    Rect(x, y, 30, 200, fill='sienna', align='center')
    RegularPolygon(x, y + 20, 50, 3, fill='forestGreen')
    RegularPolygon(x, y - 20, 50, 3, fill='forestGreen')
    RegularPolygon(x, y - 60, 50, 3, fill='forestGreen')
    RegularPolygon(x, y - 100, 50, 3, fill='forestGreen')

Circle(55, 110, 10, fill='sienna')
Circle(55, 110, 8, fill='tan')
Line(56, 105, 61, 114, dashes=(2, 3))
RegularPolygon(54, 110, 3, 3, fill='grey')

drawTree(200, 160)
drawTree(120, 280)
drawTree(290, 200)
drawTree(30, 220)
drawTree(380, 300)

flashlight = Circle(200, 200, 550, fill=None, border='black', borderWidth=500,
                    opacity=90)

def onMouseMove(mouseX, mouseY):
    # Move the flashlight with the mouse.
    ### Place Your Code Here ###
    flashlight.centerX = mouseX
    flashlight.centerY = mouseY
    pass

def onMousePress(mouseX, mouseY):
    # Whenever the mouse is pressed, change the flashlight's size.
    ### (HINT: Increase the flashight radius by 20. If it gets larger than
    #          600, reset the radius to its original value.)
    ### Place Your Code Here ###
    if (flashlight.radius < 590):
        flashlight.radius += 20
    else:
        flashlight.radius = 550
    pass

cmu_graphics.run()