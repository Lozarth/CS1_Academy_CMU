# background
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# string
Line(200, 330, 200, 400, fill='white', lineWidth=5, dashes=True)

# balloon
RegularPolygon(200, 370, 20, 3, fill='crimson')
Oval(200, 185, 300, 340,
     fill=gradient('lightCoral', 'crimson', start='right-top'))

def onMousePress(mouseX, mouseY):
    # Draw the pin.
    ### Place Your Code Here ###
    Line(
        mouseX, mouseY,
        mouseX + 40, mouseY - 20,
        
        lineWidth = 1
    )
    
    Circle(
        mouseX + 40, mouseY - 20,
        5,
        
        fill = 'blue'
    )
    
    pass

def onMouseRelease(mouseX, mouseY):
    # Pop the balloon.
    ### Place Your Code Here ###
    Star(
        200, 200,
        210,
        9,
        
        fill = 'grey',
        roundness = 10
    )
    
    Star(
        200, 200,
        190,
        9,
        
        fill = 'lightSkyBlue',
        roundness = 70
    )
    
    pass
