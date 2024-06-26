from cmu_graphics import *



app.background = gradient('deepSkyBlue', 'skyBlue', start='top')

# labels
springLabel = Label('Spring', 10, 320, fill='lightPink', size=30, align='left')
summerLabel = Label('Summer', 10, 360, fill='forestGreen', size=30, align='left')
fallLabel = Label('Fall', 390, 320, fill='darkOrange', size=30, align='right')
winterLabel = Label('Winter', 390, 360, fill='white', size=30, align='right')

leaves = Star(200, 150, 150, 16, fill='forestGreen', roundness=90)

# tree trunk and limbs
Polygon(200, 100, 150, 400, 250, 400, fill='saddleBrown')
Polygon(200, 300, 200, 250, 300, 175, fill='saddleBrown')
Polygon(200, 300, 200, 250, 100, 150, fill='saddleBrown')
Polygon(200, 200, 200, 175, 125, 100, fill='saddleBrown')
Polygon(200, 250, 200, 200, 275, 100, fill='saddleBrown')

ground = Polygon(115, 400, 140, 380, 170, 390, 210, 385, 235, 390, 275, 390,
                 295, 400, visible=False)

def onMousePress(mouseX, mouseY):
    # If a label is clicked, make the color of the leaves match the color of
    # that label. Change the leaves and ground visibility when needed.
    ### (HINT: Use contains to check what label you clicked.)
    ### Place Your Code Here ###
    if (springLabel.contains(mouseX, mouseY)):
        leaves.fill = 'lightPink'
        ground.visible = False
    elif (summerLabel.contains(mouseX, mouseY)):
        leaves.fill = 'forestGreen'
        ground.visible = False
    elif (fallLabel.contains(mouseX, mouseY)):
        leaves.fill = 'darkOrange'
        ground.fill = 'fireBrick'
        ground.visible = True
    elif (winterLabel.contains(mouseX, mouseY)):
        leaves.fill = 'white'
        ground.fill = 'white'
        ground.visible = True
        
    pass

cmu_graphics.run()