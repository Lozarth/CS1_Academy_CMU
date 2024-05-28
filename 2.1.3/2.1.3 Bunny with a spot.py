from cmu_graphics import *



def drawBunny(bunnyColor):
    Rect(0, 0, 400, 400, fill=gradient('dodgerBlue', 'deepSkyBlue'))

    # Change the ears below to use the parameter of the function as the fill.
    ### Fix Your Code Here ###
    Oval(155, 110, 60, 170, fill = bunnyColor)
    Oval(245, 110, 60, 170, fill = bunnyColor)
    Oval(155, 115, 40, 140, fill=gradient('seashell', 'wheat', start='bottom'))
    Oval(245, 115, 40, 140, fill=gradient('seashell', 'wheat', start='bottom'))

    # head
    Oval(200, 230, 200, 160, fill='white')
    Circle(150, 300, 80, fill='white')
    Circle(250, 300, 80, fill='white')

    # nose
    Polygon(180, 310, 220, 310, 200, 350)

    # Draw the spot around the eye.
    ### Place Your Code Here ###
    Oval(
        250, 270,
        60, 100,
        
        fill = bunnyColor
    )

    # eyes
    Oval(150, 275, 30, 50)
    Oval(150, 270, 10, 20, fill='white')
    Oval(250, 275, 30, 50)
    Oval(250, 270, 10, 20, fill='white')

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawBunny('pink')

cmu_graphics.run()