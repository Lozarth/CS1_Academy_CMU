app.background = 'black'

Line(200, 0, 200, 400, fill='white')
Line(0, 200, 400, 200, fill='white')

def onMouseMove(mouseX, mouseY):
    # Depending on the quadrant the mouse is on, draw a gradient line from
    # the closest corner.
    ### (HINT: Check x and y location separately to determine quadrant.)
    ### Place Your Code Here ###
    if (mouseX < 200 and mouseY < 200):
        Line(0, 0, mouseX, mouseY, lineWidth = 2, fill = gradient('red', 'black'))
    
    if (mouseX > 200 and mouseY < 200):
        Line(400, 0, mouseX, mouseY, lineWidth = 2, fill = gradient('green', 'black'))
    
    if (mouseX < 200 and mouseY > 200):
        Line(0, 400, mouseX, mouseY, lineWidth = 2, fill = gradient('blue', 'black'))
        
    if (mouseX > 200 and mouseY > 200):
        Line (400, 400, mouseX, mouseY, lineWidth = 2, fill = gradient('yellow', 'black'))
    
    pass
