Rect(0, 0, 400, 400, fill='goldenrod')

# pan
Line(105, 305, 0, 400, fill='dimGrey', lineWidth=40)
Circle(200, 200, 145, fill=rgb(60, 60, 60), border='darkGrey', borderWidth=10)
Circle(200, 200, 135, fill=None,
       border=gradient('black', 'black', 'black', 'dimGrey'), borderWidth=20)

def drawEgg(opacity):
    # Draw the egg, using the opacity provided to the function.
    ### Place Your Code Here ###
    
    # Whites
    Oval(
        230, 220,
        100, 120,
        
        fill = 'white',
        opacity = opacity
    )
    
    # Yolk
    Circle(
        220, 220,
        20,
        
        fill = 'gold',
        opacity = opacity
    )

    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawEgg(100)
