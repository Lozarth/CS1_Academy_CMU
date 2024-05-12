app.background = gradient('midnightBlue', 'dodgerBlue', start='top')

# Define the platform and ball variables.
### (HINT: You can't see the left-top of the platform so try to position it by
#          using a different alignment!)
### Fix Your Code Here ###
platform = Rect(
    -50, 150,
    300, 300,
    
    fill = gradient('grey', 'gainsboro', start = 'top-left')
)
ball = Circle(
    100, 130,
    20,
    
    fill = 'crimson'
)

yLimit = 69

def onMousePress(mouseX, mouseY):
    # Rotate the platform and bounce the ball.
    ### (HINT: Change the ball's bottom so that it matches the platform's top.)
    ### Place Your Code Here ###
    platform.rotateAngle -= 10
    ball.bottom = platform.top
    pass
