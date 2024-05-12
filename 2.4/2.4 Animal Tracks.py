# background color
app.background = gradient('wheat', 'tan', start='top')

def onMousePress(mouseX, mouseY):
    # Draw the mysterious animal's paw prints composed of two ovals and
    # three regular polygons on top
    ### Place Your Code Here ###
    
    Oval(
        mouseX, mouseY + 15,
        40, 25,
        
        fill = 'darkGray',
        opacity = 90
    )
    
    Oval(
        mouseX, mouseY + 25,
        30, 25,
        
        fill = 'darkGray',
        opacity = 80
    )
    
    RegularPolygon(
        mouseX -  20, mouseY,
        7,
        3,
        rotateAngle = 90,
        
        fill = 'darkGray'
    )
    
    RegularPolygon(
        mouseX, mouseY - 8,
        10,
        3,
        
        fill = 'darkGray'
    )
    
    RegularPolygon(
        mouseX +  20, mouseY,
        7,
        3,
        rotateAngle = 30,
        
        fill = 'darkGray'
    )
    
    
    
    pass
