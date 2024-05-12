app.enterPressed = False

Rect(0, 0, 400, 400, border='dimGrey', borderWidth=40)
Label('System Loading...', 70, 75, fill='lime', size=18, align='left')
Label('Accepting Inputs:', 70, 100, fill='lime', size=18, align='left')

msg = Label('> ', 90, 140, fill='lime', size=20, font='montserrat', align='left')

def reply():
    if (msg.value == '> python hello_world.py'):
        reply = 'Good Evening, Earth'
    else:
        reply = 'Error: file not found'

    Label(reply, 90, 200, fill='lime', size=18, font='orbitron', align='left')

def onKeyPress(key):
    # Until the enter key is pressed, do the following:
    #   - Add a space to the msg Label when the space key is pressed.
    #   - Draw the computer's reply when the enter key is pressed.
    #   - Otherwise, if the key isn't backspace, add the key to the msg Label.
    # Keep the msg Label aligned so its left is always at x=90.
    ### (HINT: You can use label.value += key or label.value += 'a' to add the
    #          key or text to a Label!)
    ### (HINT: There is a helper function defined for you above.)
    ### Place Your Code Here ###
    if (key == 'space'):
        msg.value += ' '
        msg.left = 90
    elif (key == 'enter'):
        reply()
    else:
        msg.value += key
        msg.left = 90
    pass
