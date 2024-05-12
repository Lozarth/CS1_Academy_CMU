Rect(0, 0, 400, 400, fill='aliceBlue')

def draw3DLabel(text):
    # Draw two labels, one centered slightly to the right of the other.
    ### Place Your Code Here ###
    
    Label(
        text,
        205, 200,
        
        size = 65,
        bold = True,
        font = 'arial',
        fill = 'darkGreen'
    )
    
    Label(
        text, 
        200, 200,
        
        size = 65,
        bold = True,
        font = 'arial',
        fill = 'limeGreen'
    )
    
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
draw3DLabel('Hello World')
