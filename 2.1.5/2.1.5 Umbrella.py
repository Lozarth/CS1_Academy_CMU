from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill='aliceBlue')
Line(0, 200, 400, 200, fill='lightBlue', lineWidth=400, dashes=(1, 10))

def drawUmbrella(color):
    # end tip
    Circle(200, 75, 8, fill='darkGray')

    # Change the umbrella canopy to use the function parameter as the fill.
    ### Fix Your Code Here ###
    Oval(200, 175, 300, 200, fill=color)

    # covers the Oval to create the canopy shape
    Rect(50, 175, 300, 225, fill='aliceBlue')

    # shaft
    Rect(195, 175, 10, 150, fill='saddleBrown')

    # Add code to draw the handle!
    ### Place Your Code Here ###

    Circle(
        180, 325,
        25,
        
        fill = color
    )
    
    Circle(
        180, 325,
        15,
        
        fill = 'aliceBlue'
    )
    
    Polygon(
        155, 300,
        195, 300,
        195, 320,
        155, 320,
        
        fill = 'aliceBlue'
    )
    

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawUmbrella('tomato')

cmu_graphics.run()