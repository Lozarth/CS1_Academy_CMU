from cmu_graphics import *




app.background = 'lavenderBlush'
app.isMouthGrowing = False

noiseLines = Star(160, 220, 60, 8, roundness=10)
Rect(100, 140, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
Circle(80, 50, 15)

mouth = Polygon(145, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush')

def onKeyHold(keys):
    # Depending on the variable app.isMouthGrowing, change the mouth's size,
    # reposition it on the boundary of the face, and change noiseLines.
    ### Place Your Code Here ###
    if (app.isMouthGrowing):
        mouth.width += 5
        mouth.height += 5
        noiseLines.radius +=5
    else:
        mouth.width -= 5
        mouth.height -= 5
        noiseLines.radius -= 5
        
    mouth.right = 145
        
    # Switch app.isMouthGrowing when the size of the mouth is too big or small.
    ### (HINT: Use the test cases to help figure out when too big and too
    #          small are!)
    ### Place Your Code Here ###
    # max is 70 min is 10
    if (mouth.width == 70):
        app.isMouthGrowing = False
    elif (mouth.width == 10):
        app.isMouthGrowing = True
            
    
    pass

cmu_graphics.run()