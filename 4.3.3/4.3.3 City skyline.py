from cmu_graphics import *



app.background = gradient(rgb(210, 105, 100), rgb(240, 210, 185), start='top')

mainBuilding = Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300,
                       250, 120, 230, 120, 230, 100, 210, 100, 210, 80, 205, 80,
                       200, 5, 195, 80, 190, 80, 190, 100, 170, 100, 170, 120,
                       150, 120, 150, 300, 120, 300, 120, 340, 110, 340,
                       fill=gradient(rgb(40, 25, 40), rgb(75, 55, 75),
                                     start='left'))

Star(350, 200, 50, 500, fill=gradient('papayaWhip', 'moccasin'), roundness=80)

def drawBuilding(centerX, height):
    Rect(centerX, height + 10, 60, 400 - height, align='top',
         fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))
    Polygon(centerX, height - 50, centerX - 30, height + 10,
            centerX + 30, height + 10,
            fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))

def onMousePress(mouseX, mouseY):
    # Draw a building behind the main building.
    ### Place Your Code Here ###
    drawBuilding(mouseX, mouseY)
    mainBuilding.toFront()
    pass

cmu_graphics.run()