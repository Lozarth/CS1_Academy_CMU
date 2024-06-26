from cmu_graphics import *



def drawButterfly(wingColor, bodyColor, patternColor1, patternColor2):
    # background
    Rect(0, 0, 400, 400, fill=gradient(patternColor1, patternColor2), opacity=20)

    # Use the function parameters to change the hardcoded colors below.
    ### (HINT: Take a look at how the background is drawn using patternColor1
    #          and patternColor2 above!)
    ### Fix Your Code Here ###

    # wing base shapes and antenna
    Polygon(200, 180, 370, 50, 300, 230, 200, 200, 280, 250, 250, 300, 200, 210, fill = wingColor)
    Polygon(200, 180, 30, 50, 100, 230, 200, 200, 120, 250, 150, 300, 200, 210, fill = wingColor)
    Line(200, 180, 210, 160, lineWidth=4, fill = wingColor)
    Line(200, 180, 190, 160, lineWidth=4, fill = wingColor)

    # wing patterns
    Polygon(200, 190, 340, 90, 320, 130,
            fill=gradient(patternColor1, patternColor2, start='left'))
    Polygon(200, 195, 310, 160, 290, 200,
            fill=gradient(patternColor1, patternColor2, start = 'right'))
    Polygon(210, 215, 250, 275, 265, 250, fill=None, borderWidth=4,
            border=gradient(patternColor1, patternColor2, start = 'right'))

    Polygon(200, 190, 60, 90, 80, 130,
            fill=gradient(patternColor1, patternColor2, start='right'))
    Polygon(200, 195, 90, 160, 110, 200,
            fill=gradient(patternColor1, patternColor2, start = 'left'))
    Polygon(190, 215, 150, 275, 135, 250, fill=None, borderWidth=4,
            border=gradient(patternColor1, patternColor2, start = 'left'))

    # body and decoration
    Oval(200, 200, 15, 50, fill=bodyColor)
    Circle(250, 300, 8, fill=bodyColor)
    Circle(150, 300, 8, fill=bodyColor)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawButterfly('navy', 'purple', 'dodgerBlue', 'indigo')

cmu_graphics.run()