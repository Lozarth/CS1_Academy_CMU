from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill=gradient('ghostWhite', 'powderBlue'))

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('dimGray', 'silver', 'silver', start='left-bottom'))

def onMousePress(mouseX, mouseY):
    # Draw a flower where you click the mouse and connect its stem to the vase!
    ### Place Your Code Here ###
    
    # Stem
    
    Line(
        mouseX, mouseY,
        200, 300,
        
        fill = 'limeGreen',
        lineWidth = 5
    )
    
    # Petals
    Star(
        mouseX, mouseY,
        20,
        6,
        
        fill = 'hotPink',
        roundness = 70
    )
    
    # Corona
    Circle(
        mouseX, mouseY,
        8,
        
        fill = gradient('orange', 'yellow')
    )
    
    
    
    pass

cmu_graphics.run()