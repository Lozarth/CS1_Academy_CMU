from cmu_graphics import *



app.background = gradient('deepSkyBlue', 'lightBlue', start='top')

sun = Circle(200, 100, 50, fill='yellow')
moon = Circle(300, 100, 50, fill=gradient('gainsboro', 'white'), opacity=70,
              visible=False)
ground = Rect(0, 300, 400, 100, fill='mediumSeaGreen')

def changeFillsAndMoon(newSkyFill, newSunFill, newGroundFill, showMoon):
    app.background = newSkyFill
    sun.fill = newSunFill
    ground.fill = newGroundFill

    # Depending on the showMoon input parameter, change the visibility of the moon.
    ### Place Your Code Here ###
    if (showMoon):
        moon.visible = True
    else:
        moon.visible = False

def onMouseMove(mouseX, mouseY):
    sun.centerX = mouseX
    sun.centerY = mouseY

    # Change the fill of the sky. Also change the moon's visibility if the
    # sun has set.
    ### (HINT: When it is night, the fill of the sun is None.)
    ### Place Your Code Here ###
    
    if (sun.centerY <= 100):
        changeFillsAndMoon(
            'lightSkyBlue',
            'yellow',
            'mediumSeaGreen',
            False
        )
    elif (sun.centerY <= 250):
        changeFillsAndMoon(
            gradient('deepSkyBlue', 'lightBlue', start = 'top'),
            'yellow',
            'mediumSeaGreen',
            False
        )
    elif (sun.centerY <= 350):
        changeFillsAndMoon(
            gradient('skyBlue', 'lightPink', start = 'top'),
            'gold',
            'seaGreen',
            False
        )
    elif (sun.centerY > 350):
        changeFillsAndMoon(
            gradient('black', 'midnightBlue', start = 'top'),
            None,
            'darkGreen',
            True
        )

cmu_graphics.run()