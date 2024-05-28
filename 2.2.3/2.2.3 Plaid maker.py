from cmu_graphics import *



# background
Rect(0, 0, 400, 400,
     fill=gradient('darkBlue', 'teal', 'teal', 'darkGreen', start='left-top'))

def onMousePress(mouseX, mouseY):
    # Draw two lines, one vertical and one horizontal that intersect where
    # the mouse is pressed.
    ### Place Your Code Here ###
    
    # Horizontal line
    Line(
        0, mouseY,
        400, mouseY,
        
        fill = 'fireBrick',
        opacity = 80,
        lineWidth = 7
    )
    
    # Vertical Line
    Line(
        mouseX, 0,
        mouseX, 400,
        
        fill = 'fireBrick',
        opacity = 80,
        lineWidth = 7
    )
    
    pass

cmu_graphics.run()