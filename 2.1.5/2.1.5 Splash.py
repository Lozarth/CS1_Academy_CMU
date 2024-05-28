from cmu_graphics import *



# water
Rect(0, 0, 400, 400, fill=gradient('royalBlue', 'dodgerBlue', start='top'))

# lilypads
Circle(70, 50, 40, fill=gradient('limeGreen', 'forestGreen'))
Circle(350, 175, 30, fill=gradient('limeGreen', 'forestGreen'))
Circle(140, 355, 35, fill=gradient('limeGreen', 'forestGreen'))
Star(105, 30, 35, 3, fill='royalBlue')
Star(140, 390, 30, 3, fill='dodgerBlue')

# flower
Circle(70, 40, 8, fill=gradient('darkOrchid', 'lavender', start='left-bottom'))
Circle(50, 40, 8, fill=gradient('darkOrchid', 'lavender', start='right-bottom'))
Circle(70, 60, 8, fill=gradient('darkOrchid', 'lavender', start='left-top'))
Circle(50, 60, 8, fill=gradient('darkOrchid', 'lavender', start='right-top'))
Circle(60, 38, 8, fill=gradient('darkOrchid', 'lavender', start='bottom'))
Circle(73, 50, 8, fill=gradient('darkOrchid', 'lavender', start='left'))
Circle(60, 62, 8, fill=gradient('darkOrchid', 'lavender', start='top'))
Circle(47, 50, 8, fill=gradient('darkOrchid', 'lavender', start='right'))
Circle(60, 50, 8, fill='gold')

def drawSplash(centerX, centerY):
    # Draw a splash using four circles with different radii and opacities.
    ### Place Your Code Here ###
    
    Circle(
        centerX, centerY,
        80,
        
        fill = 'deepSkyBlue',
        opacity = 30
    )
    
    Circle(
        centerX, centerY,
        60,
        
        fill = 'deepSkyBlue',
        opacity = 50
    )
    
    Circle(
        centerX, centerY,
        40,
        
        fill = 'deepSkyBlue',
        opacity= 70
    )
    
    Circle(
        centerX, centerY,
        20,
        
        fill = 'deepSkyBlue',
        opacity = 90
    )
    
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawSplash(200, 200)

cmu_graphics.run()