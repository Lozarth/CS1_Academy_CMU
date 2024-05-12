# background
Rect(100, 300, 600, 600, fill=gradient('aqua', 'royalBlue', 'midnightBlue'),
     align='center')

cursor = Polygon(200, 190, 200, 209, 204, 205, 207, 211, 211, 209, 208, 203,
                 213, 203, border='white', borderWidth=1)

def onMouseMove(mouseX, mouseY):
    # Change the location of the cursor based on your mouse location.
    ### (HINT: The mouseX and mouseY values are given by the left-top
    #          of your own mouse. The cursor should follow your mouse but
    #          be reflected vertically.)
    ### Place Your Code Here ###
    cursor.centerX = (mouseX + 6)
    cursor.centerY = 400 - (mouseY - 10) 
    pass
