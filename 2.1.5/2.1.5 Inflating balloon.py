Rect(0, 0, 400, 400, fill='skyBlue')

def drawBalloon(inflatedAmount, lightColor, darkColor):
    # Update these shapes to use the parameters.
    ### Fix Your Code Here ###
    RegularPolygon(200, 370, 20, 3, fill=darkColor)
    Oval(200, 185, inflatedAmount, 340,
         fill=gradient(lightColor, darkColor, start='right-top'))

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawBalloon(300, 'lightSalmon', 'crimson')
