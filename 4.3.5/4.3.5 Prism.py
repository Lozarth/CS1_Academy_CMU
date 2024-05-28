from cmu_graphics import *



app.background = 'black'

rainbow = Polygon(200, 185, 200, 195, 400, 202, 400, 178,
                  fill=gradient('indigo', 'blue', 'green', 'orange', 'red',
                                start='bottom'))

prism = RegularPolygon(200, 200, 120, 3, border='white')

beam = Line(0, 265, 200, 190,
            fill=gradient('white', 'lightCyan', 'black', start='left'))

def onMousePress(mouseX, mouseY):
    # If you click on the prism, move the y coordinates of the light beam and
    # the rainbow according to where you click.
    ### Place Your Code Here ###
    if (prism.contains(mouseX, mouseY) == True):
        beam.y2 = mouseY
        rainbow.centerY = mouseY
    pass

cmu_graphics.run()