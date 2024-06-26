from cmu_graphics import *



app.background = 'lightCyan'

# seesaw support
Oval(200, 330, 300, 50, fill='moccasin'),
RegularPolygon(200, 290, 70, 3, fill=None, border='tomato', borderWidth=7)
Circle(200, 235, 15, fill='skyBlue')

# seesaw body
seesaw = Line(50, 235, 350, 235, fill='tomato', lineWidth=12)

# message
message = Label('Balanced', 200, 100, fill='salmon', size=20)

def onMouseMove(mouseX, mouseY):
    # If the mouse is on the right side of the canvas, increase the seesaw's
    # rotateAngle by 1. Otherwise decrease it.
    ### Place Your Code Here ###
    
    if (mouseX > 200):
        seesaw.rotateAngle += 1
    else:
        seesaw.rotateAngle -= 1

    # Change the message depending on if rotateAngle is negative, positive,
    # or zero.
    ### (HINT: A negative value is a number that is less than 0, a positive
    #          value is a number that is bigger than 0.)
    ### Place Your Code Here ###
    
    if (seesaw.rotateAngle == 0):
        message.value = 'Balanced'
    elif (seesaw.rotateAngle > 0):
        message.value = 'Leaning Right'
    elif (seesaw.rotateAngle < 0):
        message.value = 'Leaning Left'
    

    # If the rotateAngle is bigger than 45 or smaller than -45, reset its value
    # to 45 or -45.
    ### Place Your Code Here ###
    if (seesaw.rotateAngle > 45):
        seesaw.rotateAngle = 45
    elif (seesaw.rotateAngle < -45):
        seesaw.rotateAngle = -45
    
    pass

cmu_graphics.run()