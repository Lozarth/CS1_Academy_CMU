from cmu_graphics import *



app.background = 'peru'

# main watermelon
Oval(200, 200, 200, 250,
     fill=gradient('darkGreen', 'lime', 'darkGreen', 'lime', 'darkGreen', 'lime',
                   start='right-top'), border='saddleBrown', rotateAngle=-40)

title = Label('Fruit', 200, 30,
              fill=gradient('purple', 'red', 'yellow', 'orange', 'green',
                            start='left'), size=45, bold=True)

# watermelon insides
Rect(188, 215, 75, 250, fill='peru', rotateAngle=40, align='center')
Oval(225, 225, 20, 190, fill='red', rotateAngle=40)

# seeds
Circle(180, 280, 2)
Circle(200, 250, 2)
Circle(210, 240, 2)
Circle(230, 215, 2)
Circle(250, 200, 2)
Circle(260, 180, 2)

blade = Polygon(110, 315, 265, 85, 305, 60, 300, 100, fill='white',
                border=gradient('white', 'peru'), borderWidth=4, visible=False)

# Covers the sliced part of the watermelon.
watermelonCover = Oval(200, 200, 200, 250, border='saddleBrown', rotateAngle=-40,
                       fill=gradient('darkGreen', 'lime', 'darkGreen', 'lime',
                                     'darkGreen', 'lime', start='right-top'))

def onMouseDrag(mouseX, mouseY):
    # Show the blade, move the blade, and hide the watermelonCover.
    ### (HINT: The centerY of the blade should be the canvas width minus
    #          the current x of the mouse.)
    ### Place Your Code Here ###

    blade.visible = True
    watermelonCover.visible = False
    blade.centerX = mouseX
    blade.centerY = 400 - mouseX

    # Change the title text.
    ### Place Your Code Here ###
    title.value = 'Fruit Ninja'
    pass

def onMouseRelease(mouseX, mouseY):
    # Hides the blade and shows the whole watermelon.
    blade.visible = False
    watermelonCover.visible = True

    # Changes the title text back.
    title.value = 'Fruit'

cmu_graphics.run()