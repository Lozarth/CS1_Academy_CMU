app.background = gradient('indigo', 'lightCyan', start='top')

# table
Rect(0, 250, 400, 150, fill=gradient('peru', 'saddleBrown', start='top'))

# apple
Oval(200, 140, 110, 20, fill=gradient('orange', 'crimson', start='bottom'))
Line(200, 125, 200, 160, fill='saddleBrown', lineWidth=6)
Oval(200, 158, 100, 20, fill=rgb(200, 40, 60))
Oval(170, 230, 120, 190, fill=rgb(200, 40, 60), rotateAngle=-15)
Oval(230, 230, 120, 190, fill=rgb(200, 40, 60), rotateAngle=15)
Oval(247, 190, 14, 23, fill='tan')
Oval(245, 190, 14, 22, fill=rgb(100, 40, 40))

# worm
wormy = Rect(240, 185, 35, 10,
             fill=gradient('darkGreen', 'limeGreen', 'limeGreen', start='left'))
eye = Circle(270, 188, 1.5)

wormy.visible = False
eye.visible = False

def onMouseMove(mouseX, mouseY):
    # Make the worm come out of the apple if the mouse is on the right half of
    # the canvas.
    ### Place Your Code Here ###
    if (mouseX > 200):
        wormy.visible = True
        eye.visible = True
    else:
        wormy.visible = False
        eye.visible = False
    pass
