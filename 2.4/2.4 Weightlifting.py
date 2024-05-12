app.background = gradient(rgb(230, 120, 70), rgb(225, 215, 135), start='top')

# stick figure
Circle(200, 200, 30, fill=rgb(70, 75, 75))
Line(200, 200, 200, 300, fill=rgb(70, 75, 75), lineWidth=6)
Line(200, 300, 150, 350, fill=rgb(70, 75, 75), lineWidth=5)
Line(200, 300, 250, 350, fill=rgb(70, 75, 75), lineWidth=5)
leftArm = Line(200, 250, 125, 160, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 250, 275, 160, fill=rgb(70, 75, 75), lineWidth=5)

# Bar
Line(
    100, 160,
    300, 160,
    
    fill = gradient('gainsboro', rgb(195, 195, 200), start = 'bottom'),
    lineWidth = 6
)

def drawWeights(weight):
    # Draw the weights so that their width is equal to their weight.
    ### Place Your Code Here ###
    
    Rect(
        100 - weight, 120,
        weight,
        80,
        
        fill = rgb(70, 75, 75)
    )
    
    Line(
        100 - weight, 160,
        100, 160,
        
        fill = 'silver',
        lineWidth = 80,
        dashes = (1, 8)
    )
    
    Rect(
        300, 120,
        weight,
        80,
        
        fill = rgb(70, 75, 75)
    )
    
    Line(
        300, 160,
        300 + weight, 160,
        
        fill = 'silver',
        lineWidth = 80,
        dashes = (1, 8)
    )
