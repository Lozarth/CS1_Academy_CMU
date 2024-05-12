app.background = gradient('deepSkyBlue', 'lightCyan', start='top')

def drawBalloon(centerX, centerY, radius, color):
    Line(centerX, centerY, 200, 325, fill='silver', lineWidth=1)
    Circle(centerX, centerY, radius, fill=color)

def drawHouse(bottom):
    Rect(150, bottom - 50, 50, 50, fill='pink')
    Rect(200, bottom - 50, 50, 50, fill='limeGreen')
    Polygon(140, bottom - 50, 255, bottom - 50, 255, bottom - 100,
            150, bottom - 100, fill='mediumSlateBlue')
    Polygon(200, bottom - 40, 200, bottom - 60, 225, bottom - 90,
            250, bottom - 60, 250, bottom - 40, fill='lemonChiffon')
    Polygon(160, bottom - 60, 160, bottom - 70, 170, bottom - 80,
            180, bottom - 70, 180, bottom - 60, fill='lemonChiffon')
    Rect(175, bottom - 20, 10, 20, fill='maroon')
    Rect(150, bottom - 50, 50, 15, fill='cornflowerBlue')
    Rect(180, bottom - 130, 10, 40, fill='brown')
    Rect(225, bottom - 20, 12, 20, fill='lightGrey', border='tan', align='center')
    Rect(225, bottom - 60, 10, 18, fill='lightGrey', border='tan', align='center')
    Rect(170, bottom - 67, 5, 9, fill='lightGrey', border='tan', align='center')
    Rect(162, bottom - 15, 6, 12, fill='lightGrey', border='tan', align='center')

def drawHouseAndBalloons(balloons):
    # Draw the appropriate number of balloons.
    ### (HINT: There are a maximum of 5 balloons.)
    ### Place Your Code Here ###
    
    # yandere dev code
    if (balloons == 1):
        drawBalloon(160, 50, 50, 'indigo')
    elif (balloons == 2):
        drawBalloon(160, 50, 50, 'indigo')
        drawBalloon(200, 110, 65, 'mediumPurple')
    elif (balloons == 3):
        drawBalloon(160, 50, 50, 'indigo')
        drawBalloon(200, 110, 65, 'mediumPurple')
        drawBalloon(240, 50, 35, 'darkViolet')
    elif (balloons == 4):
        drawBalloon(160, 50, 50, 'indigo')
        drawBalloon(200, 110, 65, 'mediumPurple')
        drawBalloon(240, 50, 35, 'darkViolet')
        drawBalloon(120, 120, 40, 'mediumVioletRed')
    elif (balloons >= 5):
        drawBalloon(160, 50, 50, 'indigo')
        drawBalloon(200, 110, 65, 'mediumPurple')
        drawBalloon(240, 50, 35, 'darkViolet')
        drawBalloon(120, 120, 40, 'mediumVioletRed')
        drawBalloon(280, 120, 35, 'purple')

    # Draw the house.
    ### (HINT: The house is off the ground when there are at least 5 balloons.)
    ### Place Your Code Here ###
    
    if (balloons < 5):
        drawHouse(400)
    else:
        drawHouse(350)
    
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawHouseAndBalloons(0)
