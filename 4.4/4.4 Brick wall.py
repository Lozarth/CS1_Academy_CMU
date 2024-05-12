app.background = 'darkGrey'

app.nextX = 0
app.nextY = 380

def onKeyPress(key):
    # Draw a new brick at the location specified by the app custom properties.
    newBrick = Rect(app.nextX, app.nextY, 60, 40, fill='fireBrick', border='tan')

    # Update the app custom properties to the position of the next brick.
    ### (HINT: A row of bricks ends when the next brick's left is >= 400. And the
    #          next row starts 380 pixels to the left of the brick just drawn.)
    ### Place Your Code Here ###
    app.nextX += 60
    
    print('nextX: ', app.nextX)
    print('newBrickL: ', newBrick.left)
    
    if (app.nextX >= 400):
        app.nextX = newBrick.left - 380
        app.nextY -= 40
    pass
