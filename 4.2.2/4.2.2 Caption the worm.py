from cmu_graphics import *



app.background = 'mediumAquamarine'

# apple
Oval(215, 70, 50, 20, fill='forestGreen', rotateAngle=-45)
Oval(175, 145, 100, 150, fill='fireBrick', rotateAngle=-15)
Oval(225, 145, 100, 150, fill='fireBrick', rotateAngle=15)
Oval(150, 140, 40, 100, fill='white', rotateAngle=-10)
Oval(155, 140, 40, 100, fill='fireBrick', rotateAngle=-10)

# worm
Circle(260, 140, 30, fill='mediumAquamarine')
Oval(235, 140, 10, 20, fill='mediumSeaGreen')
Oval(245, 145, 10, 20, fill='lightGreen', rotateAngle=-10)
Oval(255, 140, 10, 20, fill='mediumSeaGreen', rotateAngle=10)
Oval(265, 145, 10, 20, fill='lightGreen', rotateAngle=-10)
Oval(275, 140, 10, 20, fill='mediumSeaGreen', rotateAngle=-20)
Line(285, 125, 280, 115, fill='paleGoldenrod')
Line(280, 115, 275, 120, fill='paleGoldenrod')
Line(295, 125, 300, 115, fill='paleGoldenrod')
Line(300, 115, 305, 120, fill='paleGoldenrod')
Circle(290, 130, 10, fill='forestGreen')
Circle(285, 125, 2)
Circle(295, 125, 2)
Circle(290, 133, 3, fill=None, border='black')

cursor = Label('|', 20, 260, fill='white', size=40)

def onKeyPress(key):
    # When the key is not 'space', draw a new label using the key where
    # the text cursor is.
    ### Place Your Code Here ###
    if (key != 'space'):
        Label(key, cursor.centerX, cursor.centerY, fill = 'white', font = 'arial', size = 40)
        
    if (cursor.centerX < 380):
        cursor.centerX += 30
    else:
        cursor.centerX = 20
        cursor.centerY += 40

    # Move the cursor.
    ### (HINT: If the new centerX of cursor is greater than 380, move it to
    #          the next line and set centerX back to the beginning of the line.)
    ### Place Your Code Here ###
    pass

cmu_graphics.run()