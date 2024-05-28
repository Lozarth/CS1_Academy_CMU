from cmu_graphics import *



app.background = 'red'

# mask ridges
Line(0, 0, 400, 400)
Line(400, 0, 0, 400)
Line(200, 0, 200, 400)
Line(0, 200, 400, 200)
Star(200, 200, 150, 9, fill=None, border='black', roundness=90)
Star(200, 200, 25, 9, fill=None, border='black', roundness=90)
Star(200, 200, 250, 9, fill=None, border='black', roundness=90)

# eyes
Oval(100, 150, 100, 200, fill='white', border='black', borderWidth=6,
     rotateAngle=-20)
Oval(300, 150, 100, 200, fill='white', border='black', borderWidth=6,
     rotateAngle=20)

def onMousePress(mouseX, mouseY):
    # Change from Spiderman to Venom.
    ### (HINT: The only thing that changes is the color.)
    ### Place Your Code Here ###
    app.background = 'black'
    pass

def onMouseRelease(mouseX, mouseY):
    # Change from Venom to Spiderman.
    ### (HINT: The only thing that changes is the color.)
    ### Place Your Code Here ###
    app.background = 'red'
    pass

cmu_graphics.run()