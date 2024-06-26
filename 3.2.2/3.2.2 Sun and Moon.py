from cmu_graphics import *



# skies
Rect(0, 0, 400, 200, fill='lightSkyBlue')
Rect(0, 200, 400, 200)

# Create variables for sun and moon here.
### Fix Your Code Here ###

# top trees
Rect(305, 190, 5, 10, fill='sienna')
Polygon(300, 190, 315, 190, 307, 160, fill='forestGreen')

Rect(335, 190, 5, 10, fill='sienna')
Polygon(330, 190, 345, 190, 337, 140, fill='forestGreen')

# bottom trees
Polygon(305, 200, 310, 200, 307, 250, fill='saddleBrown', opacity=50)
Line(305, 210, 300, 215, fill='saddleBrown', opacity=50)
Line(308, 215, 315, 220, fill='saddleBrown', opacity=50)

Polygon(335, 200, 340, 200, 337, 270, fill='saddleBrown', opacity=50)
Line(338, 215, 345, 220, fill='saddleBrown', opacity=50)
Line(335, 225, 330, 230, fill='saddleBrown', opacity=50)
Line(338, 235, 345, 240, fill='saddleBrown', opacity=50)

sun = Circle(
    100, 100,
    20,
    
    fill = 'gold'
)

moon = Circle(
    100, 300,
    20,
    
    fill = 'lightGray'
)

def onMousePress(mouseX, mouseY):
    # When the mouse press is in the sky, move the sun to the pressed location
    # and reflect the moon.
    ### (HINT: The sun's bottom should not be able to be below the bottom of
    #          the sky!)
    ### (HINT: The sun and the moon have same centerX and reflecting centerY.)
    ### Place Your Code Here ###
    
    if (mouseY < 177):
        sun.centerX = mouseX
        sun.centerY = mouseY
    
        moon.centerX = mouseX
        moon.centerY = 400 - mouseY
    
    pass

cmu_graphics.run()