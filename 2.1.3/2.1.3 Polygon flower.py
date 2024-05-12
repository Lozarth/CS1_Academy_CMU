Rect(0, 0, 400, 400, fill='skyBlue')

def drawFlower(color):
    # Change these shapes so they use the color parameter for the flower petals.
    ### Modify Your Code Here ###
    RegularPolygon(200, 300, 30, 4, fill='green')
    RegularPolygon(200, 340, 30, 4, fill='green')
    RegularPolygon(200, 380, 30, 4, fill='green')
    RegularPolygon(200, 200, 100, 4, fill=color)

    RegularPolygon(200, 200, 50, 4, fill='sienna')
    RegularPolygon(150, 150, 50, 4, fill=color)
    RegularPolygon(150, 250, 50, 4, fill=color)
    RegularPolygon(250, 150, 50, 4, fill=color)
    RegularPolygon(250, 250, 50, 4, fill=color)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawFlower('gold')
