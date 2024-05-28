from cmu_graphics import *



cursor = Rect(20, 20, 20, 20, fill='red', border='black')

def moveCursor(key):
    if (key == 'up'):
        cursor.top -= 20
    elif (key == 'down'):
        cursor.top += 20
    elif (key == 'left'):
        cursor.left -= 20
    elif (key == 'right'):
        cursor.left += 20

def changeColor(key):
    # Change the cursor's fill depending on key. Use the following matches.
    # 'r' -> 'red'
    # 'g' -> 'green'
    # 'b' -> 'blue'
    # 'k' -> 'black'
    # 'w' -> 'white'
    ### Place Your Code Here ###
    if (key == 'r'):
        cursor.fill = 'red'
    elif (key == 'g'):
        cursor.fill = 'green'
    elif (key == 'b'):
        cursor.fill = 'blue'
    elif (key == 'k'):
        cursor.fill = 'black'
    elif (key == 'w'):
        cursor.fill = 'white'
    pass

def placeRect(key):
    # When a space is pressed, place a rectangle at the location of the cursor
    # with the size and fill of the cursor.
    ### Place Your Code Here ###
    if (key == 'space'):
        Rect(
            cursor.left,
            cursor.top,
            cursor.width,
            cursor.height,
            fill = cursor.fill
        )
    pass

def onKeyPress(key):
    moveCursor(key)
    changeColor(key)
    placeRect(key)
    cursor.toFront()

cmu_graphics.run()