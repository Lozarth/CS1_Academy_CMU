from cmu_graphics import *



app.background = 'deepSkyBlue'

Line(0, 120, 400, 120, fill='darkGrey', lineWidth=90)
Rect(85, 20, 230, 360, fill=rgb(30, 30, 30))

redLight = Circle(200, 90, 50, fill='red')
yellowLight = Circle(200, 200, 50, fill='gold', opacity=30)
greenLight = Circle(200, 310, 50, fill='limeGreen', opacity=30)

def onMousePress(mouseX, mouseY):
    # Change the opacity of the lights so that the stoplight changes color when
    # the mouse is pressed!
    ### Place Your Code Here ###
    if (redLight.opacity == 100):
        redLight.opacity = 30
        greenLight.opacity = 100
    elif (greenLight.opacity == 100):
        greenLight.opacity = 30
        yellowLight.opacity = 100
    elif (yellowLight.opacity == 100):
        yellowLight.opacity = 30
        redLight.opacity = 100
    pass

cmu_graphics.run()