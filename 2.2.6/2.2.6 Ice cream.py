from cmu_graphics import *



# background
Rect(0, 0, 400, 400, fill='skyBlue')

# ice cream cone
Circle(140, 200, 80, fill='pink')
Rect(100, 280, 80, 100,
     fill=gradient('peru', 'peru', 'sandyBrown', 'peru', start='left'))
Polygon(55, 240, 230, 240, 180, 290, 100, 290,
        fill=gradient('peru', 'peru', 'sandyBrown', 'peru', start='left-top'))
Line(100, 350, 180, 350, fill='sandyBrown', lineWidth=60, dashes=(1, 15))
Line(140, 320, 140, 380, fill='sandyBrown', lineWidth=80, dashes=(1, 15))

# first scoop
Circle(75, 240, 20, fill='pink')
Circle(110, 240, 20, fill='pink')
Circle(145, 240, 20, fill='pink')
Circle(175, 240, 20, fill='pink')
Circle(210, 240, 20, fill='pink')

# second scoop
Circle(140, 105, 80, fill='sienna')
Circle(75, 168, 20, fill='sienna')
Circle(110, 168, 20, fill='sienna')
Circle(145, 168, 20, fill='sienna')
Circle(175, 168, 20, fill='sienna')
Circle(210, 168, 20, fill='sienna')

def onMousePress(mouseX, mouseY):
    # Draw the sun and add a label like in the solution.
    ### Place Your Code Here ###
    Circle(
        360, 40,
        100,
        
        fill = gradient('orange', 'yellow')
    )
    
    Label(
        'The sun is hot!',
        300, 340,
        
        fill = 'black',
        font = 'arial',
        size = 15
    )

    pass

def onMouseRelease(mouseX, mouseY):
    # Draw the ice cream drips.
    ### Place Your Code Here ###
    
    Oval(
        95, 170,
        10,
        50,
        
        fill = 'sienna'
    )
    
    Oval(
        175, 200,
        10,
        50,
        
        fill = 'sienna'
    )
    
    Oval(
        85, 255,
        10, 
        35,
        
        fill = 'pink'
    )
    
    Oval(
        140, 270,
        5,
        15,
        
        fill = 'pink'
    )
    
    Oval(
        200, 255,
        5,
        25,
        
        fill = 'pink'
    )

    # Draw a label stating the ice cream is melting.
    ### Place Your Code Here ###
    Label(
        'Your ice cream is melting!',
        300, 360,
        
        fill = 'black',
        font = 'arial',
        size = 15
    )
    pass

cmu_graphics.run()