def drawMountains():
    Polygon(0, 175, 150, 175, 50, 100, fill='steelBlue')
    Polygon(210, 175, 400, 175, 300, 100, fill='midnightBlue')
    Polygon(50, 175, 190, 175, 130, 120, fill='midnightBlue')

def drawOcean():
    Polygon(0, 285, 180, 175, 0, 175, fill='dodgerBlue')
    Polygon(0, 285, 180, 175, 190, 175, 0, 350, fill='tan')

def drawGround(groundColor):
    Rect(0, 175, 400, 225, fill=groundColor)
    Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill='grey')
    Line(200, 175, 200, 400, lineWidth=10, dashes=True,
         fill=gradient('grey', 'silver', start='top'))

def drawScene(isMountainous, isDesert, isBeach, isNightTime, destination,
              milesToGo):
    # Draws the sky.
    Rect(0, 0, 400, 175, fill='lightSkyBlue')

    # Draw the ground, mountains (if needed), and ocean (if needed) based on the
    # values of the first three parameters.
    ### Place Your Code Here ###
    
    if (isMountainous):
        drawMountains()
        drawGround('lightGreen')
    
    if (isDesert and not isMountainous):
        drawGround('burlyWood')
        
    if (isBeach and not isMountainous and not isDesert):
        drawGround('lightGreen')
        drawOcean()

    # Draws the sign board with destination and milesToGo.
    Line(290, 230, 290, 200)
    Line(370, 230, 370, 200)
    Rect(330, 200, 100, 60, fill='green', border='white', align='bottom')
    Label(destination, 330, 160, fill='white', size=16)
    Label(milesToGo, 330, 180, fill='white', size=18)

    # Make the scene darker if it is night-time.
    ### (HINT: Use the Inspector to see what was added to the canvas for this
    #          test case.)
    ### Place Your Code Here ###
    if (isNightTime):
        Rect(0, 0, 400, 400, fill = 'black', opacity = 50)
        
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawScene(True, False, False, False, 'Pittsburgh', 35)
